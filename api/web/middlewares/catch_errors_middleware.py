from aiohttp.web import middleware
from aiohttp.web import json_response


@middleware
async def catch_errors_middleware(request, handler):
    errors = []

    try:
        return await handler(request)
    except Exception as exp:
        errors.append(str(exp))

    return json_response(status=400, data={'errors': errors})
