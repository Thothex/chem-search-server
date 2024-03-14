#!/bin/bash

echo "Ожидание запуска базы данных..."

while ! nc -z database 5432; do
  sleep 0.1
done

echo "База данных запущена, выполняем миграции..."
alembic upgrade head

echo "Запуск приложения..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload