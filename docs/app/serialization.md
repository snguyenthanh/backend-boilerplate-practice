# Serialization

## Schemas

The `practice_backend/schemas/` directory contains the schemas of all resources of the projects.

It is recommended to not put all schemas in 1 file, but group them into different files according to their functionalities.

The schemas are used to validate, serialize and de-serialize inbound and outbound data.

Function `validate_request_query` in `practice_backend/utils/validation` is an example of how to use a decorator to validate a request's query parameter using these schemas.
