#!/usr/bin/env sh
INIT_FILE=/tmp/init

if [ ! -f "$INIT_FILE" ]; then
  poetry install
  touch "$INIT_FILE"
fi

poetry run fastapi run src/app.py
