# Command Line Commands

## Initialization

1. Install [Poetry](https://github.com/python-poetry/poetry)
```
pip install poetry
```

2. Install the dependencies
```
poetry install
```

## Dependencies

> Remember to run `poetry update` whenever you add a new dependency or make changes to `pyproject.toml`.

If you prefer to use the traditional `requirements.txt` file, `Poetry` could export it for both `development` and `production`:
```
./scripts/lock_requirements.sh
```

This command will generate 2 files `requirements/main.txt` (for production) and `requirements/dev.txt` (for development).

## Server

### Development

```
poetry run python app.py
```

Starts the development server and makes your application accessible at
`localhost:8000`. Changes in the application code will be hot-reloaded.

### Production

```
MODE=production poetry run python app.py
```

- Runs tests: `./scripts/test.sh`


## Testing

See the [testing documentation](../testing/README.md) for detailed information
about our testing setup!

## Unit testing

```
./scripts/test.sh
```

Tests your application with the unit tests specified in the `practice_backend/tests/` directory
throughout the application.  

## Linting

```
black .
```

Lints your code and tries to fix any errors it finds.
