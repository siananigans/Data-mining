import pytest
import json

from telnyx.http.errors.builder import build_error_response

from noc_tools.infrastructure.server.http import errors


@pytest.mark.asyncio
async def test_health_check(client):
    resp = await client.get("/health")
    assert resp.status == 200
    text = await resp.text()
    assert '{"status": "OK"}' in text


@pytest.mark.asyncio
async def test_apidocs(client):
    resp = await client.get("/apidocs/private.json")
    assert resp.status == 200
    body = await resp.json()
    assert body is not None


@pytest.mark.asyncio
async def test_errors(client, http_errors, error_codes):

    # Middleware should turn the errors into this
    # {"success": false, "status": 404, "message": "Not Found"}
    _resp_tpl = '{"success": false, "status": %d, "message": "%s"}'
    for status, data in http_errors.items():
        path, message, error_class = data
        resp = await client.get(path)
        assert resp.status == status
        text = await resp.text()
        if status in errors.ERROR_CODE_LOOKUP:
            assert text == json.dumps(
                build_error_response(errors.ERROR_CODE_LOOKUP[status], error_codes)
            )
        else:
            assert text == _resp_tpl % (status, message)
