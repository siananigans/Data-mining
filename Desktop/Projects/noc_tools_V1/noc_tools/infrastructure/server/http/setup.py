"""
Setup functions for HTTP server.
"""

import aiohttp_cors

import telnyx.http.constants
from telnyx.http import apidocs_handler_factory
from telnyx.http.middleware import (
    error_middleware_factory,
    metrics_middleware_factory,
)

from noc_tools.infrastructure.server.http.handlers import health
from noc_tools.infrastructure.server.http.errors import ERROR_HANDLERS


HEALTH = "/health"
INFO = "/info"


def _setup_routes(app):
    """Add routes to the given aiohttp app."""

    # Default cors settings.
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True, expose_headers="*", allow_headers="*"
            )
        },
    )

    # Health check.
    app.router.add_get(HEALTH, health.health_check)

    # API docs
    cors.add(
        app.router.add_get(
            "/apidocs/{filename}",
            apidocs_handler_factory("filename", telnyx.http.constants.APIDOCS_DATA)
        )
    )

    # Metadata.
    app.router.add_get(INFO, health.info)


def _setup_middlewares(app):
    """Add middlewares to the given aiohttp app."""

    app.middlewares.append(
        error_middleware_factory(
            ERROR_HANDLERS, reporter_key=telnyx.http.constants.REPORTER
        )
    )
    app.middlewares.append(metrics_middleware_factory(telnyx.http.constants.REPORTER))


def configure_app(app, startup_handler):
    """Configure the web.Application."""

    _setup_routes(app)
    _setup_middlewares(app)

    # Schedule custom startup routine.
    app.on_startup.append(startup_handler)


def register_dependency(app, constant_key, dependency, usecase=None):
    """Add dependencies used by the HTTP handlers."""

    if usecase is None:
        app[constant_key] = dependency
    else:
        if constant_key not in app:
            app[constant_key] = {}
        app[constant_key][usecase] = dependency
