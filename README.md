# Backend Exercise

### Overview
This repository contains an exercise focused on creating Jupyter-like notebooks using Flask 
and PostgreSQL. The project took approximately 4-5 hours to complete, spread loosely over three days. 
Additionally, some time was spent reading documentation for Flask, SQLAlchemy, Jupyter Notebook, 
and other related technologies, as I had no prior experience with them.

Given the time constraints, I focused on implementing the fundamentals, such as setting up
Docker Compose and establishing a connection to the database.

### Running Project

1. Go to the root directory `notebooks-practice`.
2. Execute `compose.yml` using `docker`.

```commandline
docker compose up --build
```

### Accessing The Server

Once all containers have successfully started, access the server using `http://127.0.0.1:5000/`.

#### Example APIs (Work In Progress)

* GET `/api/v1/notebooks`
* GET `/api/v1/steps`

### What's Been Implemented

* Flask app and Postgres docker compose set up.
* Establishing connection to the database using retry.
* Basic tables for notebooks and steps.

### Next TODOs

* Implement API logic and tests (e.g., creating a notebook).
* Properly maintain the database connection.
* Use an ORM tool like SQLAlchemy (and justify if you  don't use it).
* Use a production WSGI server.
* Implement an MVP front-end.
* Implement proper versioning checks.