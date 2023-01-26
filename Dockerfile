FROM python:buster as base
RUN pip install poetry
RUN mkdir /myapp
COPY ./poetry.lock ./pyproject.toml /myapp/
WORKDIR /myapp
RUN poetry install
COPY . /myapp
EXPOSE 5000

FROM base as production
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"

FROM base as development
ENTRYPOINT poetry run flask run --host=0.0.0.0