import platform
from sys import implementation

from practice_backend.config import MODE


# The uvloop implementation provides greater performance,
# but is not compatible with Windows or PyPy
EVENT_LOOP = (
    "uvloop"
    if implementation.name != "pypy" and platform.system() != "Windows"
    else "asyncio"
)

DEBUG = MODE != "production"

BASE_UVICORN_RUN_CONFIG = {
    "host": "127.0.0.1",
    "port": 8000,
    "http": "h11",
    "loop": EVENT_LOOP,
}

if MODE == "production":
    UVICORN_RUN_CONFIG = {
        "access_log": False,
        "workers": 2,
        "timeout-keep-alive": 10,  # Keep-alive connections: 10 seconds
    }

else:  # MODE == "development" or MODE == "testing":
    UVICORN_RUN_CONFIG = {
        "reload": True,  # Enable auto-reload
    }
