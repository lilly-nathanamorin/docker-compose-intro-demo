# docker-compose  Demo

To get started, run

`docker-compose up -d`

Then navigate to [localhost:8888](http://localhost:8888)
You can login to the admin portal at [localhost:8888/admin](http://localhost:8888/admin)
with user/pass `admin/admin`

To tear it down:

`docker-compose down -v`


## Environment

Optionally modify or set  these environment variables on the `web` service
 in the docker-compose.yml file:
 
| ENV var | options | default | description |
| :---: | :---: | :---: | :---: |
| `DJANGO_SECRET` | n/a | randomly generated | The Django Secret to use. Default will randomly generate one. Cannot use this default in production as user password encryption will break on each deployment. |
| `DATABASE_NAME` | n/a | `postgres` | The name of the database |
| `DATABASE_HOST` | n/a | `db` | hostname of the database, in docker-compose it is the container name |
| `DATABASE_PORT` | n/a | `5432` | port for database |
| `DATABASE_USER` | n/a | `postgres` | username for database |
| `DATABASE_PASSWORD` | n/a | `test` | password for database. In the compose stack tis is set in the environment variable `POSTGRES_PASSWORD` on the `db` service. |
