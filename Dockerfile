ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

# Don't write pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keep Python from bufferring to always emit logs.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r notebook/requirements.txt

EXPOSE 5000

# TODO: use a production wsgi server.
ENTRYPOINT ["python"]

CMD ["notebook/server.py"]