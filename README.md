Back-end Boilterplate Practice
==============================

[![Build Status](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice.svg?branch=master)](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice)
[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%20PyPy3-blue)](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice)


A template repo to learn Back-end development with Python.

## Installation

### 1. Install [Poetry](https://github.com/python-poetry/poetry)

```
pip install poetry
```

### 2. Install the dependencies

```
poetry install
```

### 3. Set up [Pre-commit](https://github.com/pre-commit/pre-commit) (for development)

> Windows users could skip this step as pre-commit is not yet supported on Windows.

```
pip install pre-commit
pre-commit install
```

## Usage

> You are also recommended to check out [other commands for Poetry](https://python-poetry.org/docs/cli/).

### To open the shell within the virtual environment:

```
poetry shell

# Run a Python file
python run app.py
```

### Run a Python file without opening a shell

```
poetry run python app.py
```

## Exercises

> To look for where to do each exercise, search for `TODO - Exercise X`, where X is the number of the exercise.


### 1. Understand the overall structure of the project

At the moment, the project only has 1 endpoint (root - `/`), unfinished helper functions for authentication and a sample for schema (using [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)).

### 2. Set up a development database

For this project, we will be using [Docker](https://www.docker.com) as a container for our database and application.

Steps:
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Read about how to create, start and stop a Docker container.
- Add `docker` commands to `scripts/dev.sh` to set up and run a Docker container for our development database.

### 3. Integrate an ORM to the app

Starlette advises using [the `databases` package](https://github.com/encode/databases), which also provides [SQLAlchemy](https://www.sqlalchemy.org) support.

I am aware that the name of the `databases` package makes it very hard to search for solutions for its problems. However, as this is a practice repo, a general-purpose library is preferred, since `databases` could support MySQL, PostgreSQL and SQLite.

### 4. Serialization with [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)

While working with data, it is compulsory to serialize and de-serialize data for the users.

This exercise only requires you to understand the concept of serialization, de-serialization and how to (basically) use [Marshmallow](https://marshmallow.readthedocs.io/en/stable/).

#### 4.1. Definitions

Serialization is the process of converting structured data to a format that allows sharing or storage of the data in a form that allows recovery of its original structure.

De-serialization is the opposite process which converts the original structure to a more readable format (usually to return to the users).

#### 4.2. Common usage of serialization

Serialization is commonly used to validate users' requests. An example is:

```
Endpoint: /search?username=helloworld&age=20

schema={
	username: 'string',
	age: 'int',
}

```

With serialization, we could convert the value of age (which is currently a string of `20`) to `integer` and verify that the query parameters (`username` and `age`) have expected data types.


#### 4.3. Common usage of de-serialization

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
