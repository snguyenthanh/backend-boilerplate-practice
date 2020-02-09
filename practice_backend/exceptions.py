from starlette.exceptions import HTTPException


class Forbidden(HTTPException):
    """
    Forbidden - 403
    Receiving a 403 response is the server telling you:
        I’m sorry. I know who you are
        but you just don’t have permission to access this resource.
    """

    def __init__(self, *, detail: str = None):
        detail = detail or "You are not allowed to perform this action."
        super().__init__(status_code=403, detail=detail)


class Unauthorized(HTTPException):
    """
    Unauthorized - 401
    A 401 Unauthorized response should be used for missing or bad authentication.
    """

    def __init__(self, *, detail: str = None):
        detail = detail or "Authentication credentials are missing are invalid."
        super().__init__(status_code=401, detail=detail)


class InvalidUsage(HTTPException):
    """
    Unauthorized - 400
    This exception can be raised for:
        - Malformed request syntax.
        - Invalid request message parameters.
        - Deceptive request routing.
        etc.
    The client SHOULD NOT repeat the request without modifications.
    """

    def __init__(self, *, detail: str = None):
        super().__init__(status_code=400, detail=detail)


class NotFound(HTTPException):
    """
    Unauthorized - 404
    This exception is raised when the requested resource is not found.
    """

    def __init__(self, *, detail: str = None):
        detail = detail or "The requested resource is not found."
        super().__init__(status_code=404, detail=detail)
