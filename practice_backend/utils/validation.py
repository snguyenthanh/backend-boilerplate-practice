from functools import partial, wraps
from marshmallow import ValidationError

from practice_backend.exceptions import InvalidUsage
import practice_backend.schemas as schemas


def validate_request_query(func=None, *, schema):
    if func is None:
        return partial(validate_request_query, schema=schema)

    @wraps(func)
    async def inner(request, *args, **kwargs):
        _schema = getattr(schemas, schema)()
        try:
            req_args = _schema.load(request.query_params)
        except ValidationError as err:
            raise InvalidUsage(detail=err.messages)

        return await func(request, req_args=req_args, *args, **kwargs)

    return inner
