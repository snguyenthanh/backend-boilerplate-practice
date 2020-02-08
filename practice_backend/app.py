from starlette.applications import Starlette
from starlette.responses import UJSONResponse
from starlette.routing import Route
import uvicorn


async def homepage(request):
    return UJSONResponse({"hello": "world"})


app = Starlette(debug=True, routes=[Route("/", homepage),])

if __name__ == "__main__":
    uvicorn.run(
        "app:app", host="127.0.0.1", port=8000, http="h11", loop="asyncio"
    )
