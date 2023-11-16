FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

RUN pip install poetry && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

CMD ["python", "manage.py", "runserver"]
