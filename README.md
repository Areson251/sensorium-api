# Sensorium API

## Локальный запуск
Прежде всего необходимо установить [Docker](https://docs.docker.com/engine/install/).

Для запуска приложения:

```bash
$ docker compose up
```

Оно будет запущено на [`http://localhost:8000`](http://localhost:8000).

Документация API доступна по следующему адресу: [`http://localhost:8000/api/schema/swagger-ui/`](http://localhost:8000/api/schema/swagger-ui/).

## Разработка API

Для локальной разработки необходимо установить [poetry](https://python-poetry.org/):

```bash
$ sudo apt update
$ sudo apt install -y curl
$ curl -sSL https://install.python-poetry.org | python3 -
```

После установки поетри, необходимо его настроить:

```bash
$ poetry config virtualenvs.in-project true
```

Далее необходимо установить зависимости проекта:

```bash
$ poetry install
```
# sensorium-api
