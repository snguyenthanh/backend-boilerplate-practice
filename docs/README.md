# Documentation

## Table of Contents

- [General](general)
  - [CLI Commands](general/commands.md)
  - [Tool Configuration](general/tools.md)
  - [Server Configurations](general/server-configs.md)
  - [Deployment](general/deployment.md) _# TODO_
- [Testing](testing) _# TODO_
- [Your app](app)
  - [Serialization](app/serialization.md)
  - [Authentication](app/authentication.md)	_# TODO_
  - [routing](app/routing.md)
- [Exercises](exercises)

## Overview

### Installation

Ensure that you are in the directory of this repo before running these commands.

1. Install [Poetry](https://github.com/python-poetry/poetry)
```
pip install poetry
```

2. Install the dependencies
```
poetry install
```

3. Set up [Pre-commit](https://github.com/pre-commit/pre-commit) (for development)
```
pip install pre-commit
pre-commit install
```
Windows users could skip this step as pre-commit is not yet supported on Windows.


### Usage

> You are also recommended to check out [other commands for Poetry](https://python-poetry.org/docs/cli/).

#### To open the shell within the virtual environment:
```
poetry shell

# Run a Python file
python run app.py
```

#### Run a Python file without opening a shell
```
poetry run python app.py
```

### Structure

The [`practice_backend/`](../../../tree/master/practice_backend) directory contains your entire application code, including tests.

The [`requirements/`](../../../tree/master/requirements) directory contains the dependencies of the app for both development and production.

the [`scripts/`](../../../tree/master/scripts) directory contains the Bash files (CLI) to make your life easier.

The remaining configuration files (including `*.yml`, `*.yaml` and `*.toml`) are covered in [Tool Configuration](general/files.md).


### Development

Run `./scripts/dev.sh` to see your app at `localhost:8000`.

### Build & Deploy

1. (Optional) Set up your production machine with [Server Configurations](general/server-configs.md).

2. In your production machine, set the following environment variables:
```
MODE=production
```

3. Run the `app.py`
```
poetry run python app.py
```

You could also [check out other deployment methods with Uvicorn](https://www.uvicorn.org/deployment).

### Testing _(TODO)_

For a thorough explanation of the testing procedure, see the
[testing documentation](testing/README.md)!
