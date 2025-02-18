FROM python:3.13

WORKDIR /code

COPY . /code
COPY ./entrypoint.sh /usr/local/bin

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=2.1.0

RUN pip install poetry \
    && poetry install

ENTRYPOINT ["entrypoint.sh"]