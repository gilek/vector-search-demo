#!/usr/bin/env sh

if [ ! -f dist/bundle.js ]; then
  yarn install
  yarn build
fi

http-server dist
