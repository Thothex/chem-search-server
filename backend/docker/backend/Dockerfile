FROM python:3.10-slim


SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

RUN pip install --upgrade pip

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./docker/backend/entrypoint.sh"]
CMD ./docker/backend/entrypoint.sh