FROM node:23

WORKDIR /code

COPY ./entrypoint.sh /usr/local/bin

RUN yarn global add http-server

ENTRYPOINT ["entrypoint.sh"]