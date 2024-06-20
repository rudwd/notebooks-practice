# Minimal Flask Backend with PostgreSQL Exercise

### Overview
The repository serves as both an exercise and a demonstration of the bare minimum code 
needed to set up a Flask app with PostgreSQL in containers. It focuses on the fundamentals, 
such as the minimum Docker Compose configuration and establishing a connection from 
the Flask app to the database.

### Running Project

1. Go to the root directory `notebooks-practice`.
2. Execute `compose.yml` using `docker`.

```commandline
docker compose up --build
```

### Accessing The Server

Once all containers have successfully started, access the server using `http://127.0.0.1:5000/`.

#### Example (Dummy) APIs

* GET `/api/v1/notebooks`
* GET `/api/v1/steps`

### What's Been Implemented

* Flask app and Postgres Docker compose set up.
* Establishing connection to the database using retry.
* Minimal configuration.
* Basic queries for creating database tables.
* Basic versioning.

### Next 

* Implement API logic and tests (e.g., creating a notebook).
* Properly maintain the database connection.
* Use an ORM tool like SQLAlchemy (and justify if you  don't use it).
* Use a production WSGI server.
* Implement an MVP front-end.
* Implement proper versioning checks.