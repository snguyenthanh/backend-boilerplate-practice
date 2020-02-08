#!/bin/bash

# Run a local dev environment
set -e
export MODE=development

# Set up DB or related services
# ...

# Run the Python app
poetry run python app.py &
# pipenv run hypercorn --keep-alive 10 --workers 3 --bind 127.0.0.1:8000 app:app

# Allow both the Postgres container and Python app
# to run in parallel
wait
