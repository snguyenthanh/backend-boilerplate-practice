from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
    AuthCredentials,
)


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        scheme, credentials = auth.split()
        if scheme.lower() != "basic":
            return

        # TODO: Exercise 3
        # Hash the password using passlib[bcrypt]
        # and verify the username and password with a database.
        return AuthCredentials(["authenticated"]), SimpleUser(username)
