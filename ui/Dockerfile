FROM node:23

WORKDIR /code
COPY . /code

RUN yarn install \
    && yarn run build \
    && rm -fr node-modules

RUN yarn global add http-server

CMD ["http-server", "dist"]