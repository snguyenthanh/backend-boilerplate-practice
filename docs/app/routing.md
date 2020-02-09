# Routing

All the accessible endpoints are located at `practice_backend/views/urls.py`.

Each sub-route (such as `/users`) should have a corresponding filename in `practice_backend/views/` directory, such as route `/users` is under file `practice_backend/views/users.py`.

The `routes` variable of each sub-route is to be put at the end of each `views` file, and be imported by `practice_backend/views/urls.py` to be mounted.

```
from practice_backend.views.users import routes as users_routes


routes = [
    Mount("/", routes=root_routes),
		Mount("/users", routes=users_routes),
]
```

More details can be found in [Starlette's Routing documentation](https://www.starlette.io/routing).
