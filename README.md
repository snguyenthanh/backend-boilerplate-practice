Back-end Boilerplate Practice
==============================

[![Build Status](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice.svg?branch=master)](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice)
[![Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%20PyPy3-blue)](https://travis-ci.org/snguyenthanh/backend-boilerplate-practice)


Learn modern Back-end development with Python.

## Quick start

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

4. Run the project
```
poetry run python app.py
```

## Documentation
- [**Overview**](docs/README.md): A short overview of the included tools.
- [**Tools**](docs/general/tools.md): An overview of the configuration files of this project (including `Tox` and `Poetry`).
- [**Exercises**](docs/exercises/README.md): Learn how to build a back-end project from ground up.
