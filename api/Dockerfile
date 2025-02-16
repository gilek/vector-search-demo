FROM python:3.13

WORKDIR /code
COPY . /code

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=2.1.0

RUN pip install poetry \
    && poetry install

CMD ["poetry", "run", "fastapi", "run", "src/app.py"]
