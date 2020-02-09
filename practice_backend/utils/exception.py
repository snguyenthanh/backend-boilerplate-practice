from starlette.responses import UJSONResponse


async def http_exception(request, exc):
    return UJSONResponse({"msg": exc.detail}, status_code=exc.status_code)
