#!/bin/bash

set -e

poetry export -f requirements.txt --without-hashes > requirements/main.txt
poetry export -f requirements.txt --dev --without-hashes > requirements/dev.txt
