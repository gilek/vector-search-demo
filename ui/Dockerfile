FROM python:3.13

WORKDIR /code

RUN yarn install \
    && yarn run build \
    && rm -fr node-modules

RUN yarn global add http-server

ENTRYPOINT entrypoint.