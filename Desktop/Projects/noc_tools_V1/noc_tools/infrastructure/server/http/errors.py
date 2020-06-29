"""
Custom, JSON-formatted HTTP errors.
"""

import json

from aiohttp import web

from telnyx.http import constants
from telnyx.http.errors.builder import build_error_response
from telnyx.http.errors.codes.general import (
    INVALID_REQUEST_400,
    UNAUTHORIZED,
    FORBIDDEN,
    RESOURCE_NOT_FOUND,
    INVALID_REQUEST_415,
    SERVER_ERROR,
)


async def api_error_handler(
    request: web.Request, response: web.Response
) -> web.Response:
    """Provide an API-friendly error message.

    The body can either be a simple text message, in which case it is sent as the "message" field.

    Otherwise the body is JSON-encoded data containing two fields:
        message: A summary description of the error.
        reasons: A dict, in which the keys are components, and the values are lists of error
            messages.

    Because API "helpfully" adds a period at the end of an error message, we strip them out here.
    """

    try:
        err_data = json.loads(response.text)  # Might not be JSON.
        if not isinstance(err_data, dict):
            raise ValueError  # If JSON, must be a object/dict.

        return web.json_response(err_data, status=response.status)

    except (json.JSONDecodeError, ValueError):
        error_codes = request.app[constants.API_ERROR_CODES]
        if response.status in ERROR_CODE_LOOKUP:
            errors = build_error_response(
                ERROR_CODE_LOOKUP[response.status], error_codes
            )
        else:
            errors = {
                "success": False,
                "status": response.status,
                "message": response.text.rstrip("."),
            }

        # Preserve headers, but force to JSON
        headers = {k: v for k, v in response.headers.items() if k != "Content-Type"}
        return web.json_response(errors, status=response.status, headers=headers)


ERROR_HANDLERS = {
    400: api_error_handler,
    401: api_error_handler,
    403: api_error_handler,
    404: api_error_handler,
    409: api_error_handler,
    415: api_error_handler,
    500: api_error_handler,
    503: api_error_handler,
}


ERROR_CODE_LOOKUP = {
    400: INVALID_REQUEST_400,
    401: UNAUTHORIZED,
    403: FORBIDDEN,
    404: RESOURCE_NOT_FOUND,
    415: INVALID_REQUEST_415,
    500: SERVER_ERROR,
}
