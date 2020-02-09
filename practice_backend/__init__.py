from starlette.applications import Starlette
from starlette.authentication import AuthCredentials
from starlette.exceptions import HTTPException
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from practice_backend.config.app import DEBUG
from practice_backend.middlewares.authentication import AuthBackend
from practice_backend.views.urls import routes
from practice_backend.utils.exception import http_exception


def create_app():
    middleware = [Middleware(AuthenticationMiddleware, backend=AuthBackend())]
    exception_handlers = {HTTPException: http_exception}
    app = Starlette(
        routes=routes,
        debug=DEBUG,
        middleware=middleware,
        exception_handlers=exception_handlers,
    )
    return app
