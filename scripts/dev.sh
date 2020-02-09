#!/bin/bash

# Run a local dev environment
set -e
export MODE=development

# TODO - Exercise 2
# Set up DB or related services
# ...

# Run the Python app
poetry run python app.py &

# Allow both the DB container and Python app to run in parallel
wait
