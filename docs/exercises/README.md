# Exercises

> To look for where to do each exercise, search for `TODO - Exercise X`, where X is the number of the exercise.


## 1. Understand the overall structure of the project

At the moment, the project only has 1 endpoint (root - `/`), unfinished helper functions for authentication and a sample for schema (using [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)).

## 2. Set up a development database

For this project, we will be using [Docker](https://www.docker.com) as a container for our database and application.

Steps:
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Read about how to create, start and stop a Docker container.
- Add `docker` commands to `scripts/dev.sh` to set up and run a Docker container for our development database.

## 3. Integrate an ORM to the app

Starlette advises using [the `databases` package](https://github.com/encode/databases), which also provides [SQLAlchemy](https://www.sqlalchemy.org) support.

I am aware that the name of the `databases` package makes it very hard to search for solutions for its problems. However, as this is a practice repo, a general-purpose library is preferred, since `databases` could support MySQL, PostgreSQL and SQLite.

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


### 4.3. Common usage of de-serialization

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
