from starlette.routing import Mount

from practice_backend.views.root import routes as root_routes


routes = [
    Mount("/", routes=root_routes),
]
