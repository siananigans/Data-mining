"""
noc_tools

Service to host tools for NOC and Telnyx to use for troubleshooting.
"""
import argparse
import asyncio
import json
import logging
import os
import signal
import socket
import sys
from typing import Mapping

from aiohttp import web
from aiotelegraf import statsd
import bugsnag

from telnyx.apidocs import load_apidocs
from telnyx.http import constants as telnyx_http_constants
from telnyx.reporter import BugsnagReporter
from telnyx.util import new_short_id, Socket

from noc_tools.infrastructure.server import http


def on_startup(conf: Mapping, error_codes: Mapping):
    """Return a startup handler that will bootstrap and then begin background tasks."""

    async def startup_handler(app):
        """Run all initialization tasks.

        These are tasks that should be run after the event loop has been started but before the HTTP
        server has been started.
        """

        # Pull configuration settings.
        app_name = conf["runtime"]["app_name"]
        hostname = conf["runtime"]["hostname"]
        # suffix = conf["runtime"]["suffix"]
        telegraf_conn = Socket.from_str(conf["statsd"])

        # Load API docs.
        apidocs_data = load_apidocs(conf["apidocs"]["filepath"], conf["apidocs"]["filenames"])

        # Initialize dependencies.
        # client_session = aiohttp.ClientSession()  # Shared HTTP ClientSession.
        metrics = await statsd.new(
            telegraf_conn.host,
            telegraf_conn.port,
            logging.getLogger("metrics"),
            default_tags={"host": hostname},
        )

        reporter = BugsnagReporter(metrics, app_name)

        # Save dependencies in the HTTP app.
        http.register_dependency(app, telnyx_http_constants.APIDOCS_DATA, apidocs_data)
        http.register_dependency(
            app, telnyx_http_constants.API_ERROR_CODES, error_codes
        )
        http.register_dependency(app, telnyx_http_constants.REPORTER, reporter)

        # Define required cleanup
        async def cleanup(app):  # pylint: disable=unused-argument
            """Perform required cleanup on shutdown"""
            # await client_session.close()

        app.on_shutdown.append(cleanup)

    return startup_handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "-c",
        "--config",
        default="/etc/noc_tools.json",
        help="Configuration file",
    )
    parser.add_argument(
        "-e",
        "--errors-file",
        default=os.environ.get("ERROR_CODES_PATH", "/etc/error-codes.json"),
        help="Telnyx API Error Codes file.",
    )
    parser.add_argument(
        "--level", default=os.environ.get("LOG_LEVEL", "INFO"), help="Logging level.",
    )
    parser.add_argument(
        "--no-report", action="store_true", help="Don't report errors to Bugsnag."
    )
    args = parser.parse_args()

    # Load config.
    with open(args.config, "r") as f:
        conf = json.load(f)

    # Load errors.
    with open(args.errors_file, "r") as f:
        error_codes = json.load(f)

    # Set some runtime variables.
    hostname = os.environ.get("SERVER_HOSTNAME", socket.gethostname()).split(".", 1)[0]
    svc_id = new_short_id()
    conf["runtime"] = {
        "app_name": "noc_tools",
        "hostname": hostname,
        "id": svc_id,
        "suffix": "to.{}".format("noc_tools"),
    }

    # Initialize logger and bugsnag.
    logging.basicConfig(stream=sys.stdout, level=args.level)
    bugsnag.configure(**conf["bugsnag"])
    if args.no_report:
        # Disable Bugsnag reporting by removing all valid release stages.
        bugsnag.configure(notify_release_stages=[])

    # Initialize the HTTP server.
    http_socket = Socket.from_dict(conf["http"])
    app = web.Application()
    http.configure_app(app, on_startup(conf, error_codes))

    # Start the HTTP server.
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGTERM, loop.stop)
    web.run_app(app, host=http_socket.host, port=http_socket.port)


if __name__ == "__main__":
    sys.exit(main())
