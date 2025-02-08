FROM python:3.12-alpine

RUN pip install --no-cache-dir poetry==2.0.0

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "python", "main.py"]