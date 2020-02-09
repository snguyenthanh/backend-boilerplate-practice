# Application

## Packages

### 1. Web framework

> Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.  
  -- <cite>Starlette.io</cite>

[Starlette](https://www.starlette.io) is chosen for this project as it is a general-purpose micro-framework, has a flat learning curve and most compulsory functionalities of a web framework as built-in. On the other hand, `Flask`, for example of another micro-framework, depends heavily on its (mostly third-party) middlewares.

### 2. Serialization / Validation

This project uses [Marshmallow](https://marshmallow.readthedocs.io/en/stable) for serialization and object validation. In [the benchmarks of validation libraries provided by Pydantic](https://pydantic-docs.helpmanual.io/benchmarks), `Marshmallow` stands out as a mature, stable and extensively customizable package.


### 3. Database and ORM

This project uses [the `databases` package](https://github.com/encode/databases), which also provides [SQLAlchemy](https://www.sqlalchemy.org) support.

The name of the `databases` package makes it hard to search for solutions for its problems. However, as this is a practice repo, a general-purpose library is preferred, since `databases` could support MySQL, PostgreSQL and SQLite.

You could also use other libraries (such as [GINO](https://github.com/python-gino/gino), [Motor](https://github.com/mongodb/motor), [asyncpg](https://github.com/MagicStack/asyncpg), [aiomysql](https://github.com/aio-libs/aiomysql) or [aiosqlite](aiosqlite)) as you prefer.

### Learn more
- [Serialization](app/serialization.md)
- [Authentication](app/authentication.md)	_# TODO_
- [routing](app/routing.md)

## Architecture

This project adopts [the Application Factory Pattern](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure) (having the application to be created by function `create_app()` instead of being a global variable) and [Django's project structure](https://djangobook.com/mdj2-django-structure/).

Helper functions should be put under `practice_backend/utils/` directory to reduce the complexity of the main files, as well as to make the functions reusable.
