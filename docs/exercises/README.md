# Exercises

> To look for where to do each exercise, search for `TODO - Exercise X`, where X is the number of the exercise.

## 1. Set up a development database

For this project, we will be using [Docker](https://www.docker.com) as a container for our database and application.

Steps:
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Read about how to create, start and stop a Docker container.
- Add `docker` commands to `scripts/dev.sh` to set up and run a Docker container for our development database.

## 2. Integrate an ORM to the app

Starlette advises using [the `databases` package](https://github.com/encode/databases), which also provides [SQLAlchemy](https://www.sqlalchemy.org) support.

Integrate `databases` to `Starlette`'s app and write a `User` model and schema with the following fields:
- id: uuid (or str)
- username: str
- password: str
- role_id: int
- is_disabled: bool
- created_at: int (unix timestamp)
- updated_at: int (unix timestamp)


## 3. Authentication

1. Finish the function `authenticate` of `AuthBackend` in `practice_backend/middlewares/authentication.py`.
1. Use [the built-in decorator `requires` of `Starlette`](https://www.starlette.io/authentication) to validate that the authentication works as expected.

## 4. Serialization with [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)

While working with data, it is compulsory to serialize and de-serialize data for the users.

This exercise only requires you to understand the concept of serialization, de-serialization and how to (basically) use [Marshmallow](https://marshmallow.readthedocs.io/en/stable/).

### 4.1. Definitions

Serialization is the process of converting structured data to a format that allows sharing or storage of the data in a form that allows recovery of its original structure.

De-serialization is the opposite process which converts the original structure to a more readable format (usually to return to the users).

### 4.2. Common usage of serialization

Serialization is commonly used to validate users' requests. An example is:

```
Endpoint: /search?username=helloworld&age=20

schema={
	username: 'string',
	age: 'int',
}

```

With serialization, we could convert the value of age (which is currently a string of `20`) to `integer` and verify that the query parameters (`username` and `age`) have expected data types.


### 3.3. Common usage of de-serialization

De-serialization is commonly used to filter and parse returned data to users. An example is:
```
raw = <UserObject(name="Josh", age=20)>

deserialized_data = {
	"user": {
		"name": "Josh",
		"age": 20,
	}
}
```

### 4.4. Assignments

Implement an endpoint `/users/me` that returns the information of the logged in user, excluding the password.
