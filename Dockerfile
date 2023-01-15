FROM python:buster
RUN pip install poetry
RUN mkdir /myapp
COPY . /myapp
EXPOSE 5000
WORKDIR /myapp
RUN poetry install
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0:5000 "todo_app.app:create_app()"
