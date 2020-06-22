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
 
| ENV var | default | description |
| :---: | :---: | :---: |
| `DJANGO_SECRET` | randomly generated | The Django Secret to use. Default will randomly generate one. Cannot use this default in production as user password encryption will break on each deployment. |
| `DATABASE_NAME` | `postgres` | The name of the database |
| `DATABASE_HOST` | `db` | hostname of the database, in docker-compose it is the container name |
| `DATABASE_PORT` | `5432` | port for database |
| `DATABASE_USER` | `postgres` | username for database |
| `DATABASE_PASSWORD` | `test` | password for database. In the compose stack tis is set in the environment variable `POSTGRES_PASSWORD` on the `db` service. |
| `LOCAL_ADMIN_USER` | `admin` | in the local development, we create an admin superuser to help you get started. default username for it is admin. |
| `LOCAL_ADMIN_PASS` | `admin` | in the local development, we create an admin superuser to help you get started. default password for it is admin. | 

## Tests

To run tests, stack should be up as described above then run:

```commandline
docker exec -it web bash -c "python manage.py test"
```

## Clean Up Docker Space

It's common to fill volumes or leave networks and containers dangling that fill 
up your Docker allocated space on your machine. Make sure to use `-v` in the down 
command as shown above to try to force removal of volumes when cleaning up. 
These commands are helpful for cleaning up after yourself:

```commandline
docker volume ls -qf dangling=true | xargs docker volume rm
docker images --filter "dangling=true" -q --no-trunc | xargs docker rmi
docker ps -qa --no-trunc --filter "status=exited" | xargs docker rm
```
