FROM python:3.12-alpine

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY . .

CMD ["poetry", "run", "python", "main.py"]