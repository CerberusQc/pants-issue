FROM python:3.10-slim

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . /app
CMD ["python", "run.py"]