import asyncio
import json
import os

from aiohttp import web
from aiohttp.test_utils import TestClient as MockHTTPClient, TestServer
import pytest

from telnyx.apidocs import load_apidocs
from telnyx.http import constants as telnyx_http_constants
from telnyx.reporter.mock import MockReporter

from noc_tools.infrastructure.server import http


@pytest.fixture
def http_errors():
    return {
        400: ("/errors/400", "Bad Request", web.HTTPBadRequest),
        403: ("/errors/403", "Forbidden", web.HTTPForbidden),
        404: ("/errors/404", "Not Found", web.HTTPNotFound),
        409: ("/errors/409", "Conflict", web.HTTPConflict),
        415: ("/errors/415", "Unsupported Media Type", web.HTTPUnsupportedMediaType),
        500: ("/errors/500", "Internal Server Error", web.HTTPInternalServerError),
        503: ("/errors/503", "Service Unavailable", web.HTTPServiceUnavailable),
    }


@pytest.fixture
def error_codes():
    to_open = os.getenv("ERROR_CODES_PATH", "error-codes.json")
    with open(to_open, "r") as f:
        codes = json.load(f)
    return codes


@pytest.fixture
def apidocs_data():
    apidocs_data = load_apidocs(
        os.getenv("APIDOCS_FILEPATH", "./apidocs/"),
        ["private.json"]
    )
    return apidocs_data


@pytest.fixture
def reporter():
    return MockReporter()


@pytest.fixture
def web_app(loop, http_errors, apidocs_data, reporter, error_codes):
    async def error_resp(request):
        status = int(request.path.split("/")[2])
        path, message, error_class = http_errors[status]
        raise error_class(text=message)

    async def startup_handler(app):
        # Save dependencies in the HTTP app.
        http.register_dependency(app, telnyx_http_constants.REPORTER, reporter)
        http.register_dependency(app, telnyx_http_constants.APIDOCS_DATA, apidocs_data)
        http.register_dependency(
            app, telnyx_http_constants.API_ERROR_CODES, error_codes
        )

        # For testing purposes add routes for responses
        for status, data in http_errors.items():
            path, message, error_class = data
            app.router.add_get(path, error_resp)

    app = web.Application()
    http.setup.configure_app(app, startup_handler)
    return app


@pytest.fixture
def test_server(loop, web_app):
    return TestServer(app=web_app, loop=loop)


@pytest.fixture
async def client(aiohttp_client, web_app):
    client = await aiohttp_client(web_app)
    return client
