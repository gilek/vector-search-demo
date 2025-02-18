#!/usr/bin/env sh

if [ "$1" = "import" ]; then
  tar -xvzf tshirts.tar.gz
fi

python "$1.py"
