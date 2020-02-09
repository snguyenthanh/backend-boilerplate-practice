from starlette.authentication import requires
from starlette.responses import UJSONResponse
from starlette.routing import Route

from practice_backend.utils.validation import validate_request_query

# @requires(['authenticated'])
@validate_request_query(schema="User")
async def root(request, req_args=None):
    return UJSONResponse({"hello": "world"})


routes = [Route("/", root)]
