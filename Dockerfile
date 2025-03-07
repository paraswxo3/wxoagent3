FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]