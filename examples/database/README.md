# Database server

Nowadays we thankfully do not need to install every database we need during local development.


## PostgreSQL
As an example, we will run a local instance of PostgreSQL 12.1 using [official docker image](https://hub.docker.com/_/postgres)

### run using CLI
```bash
docker run \
        -p 5432:5432 \
        -e POSTGRES_DB=znf \
        -e POSTGRES_USER=znf \
        -e POSTGRES_PASSWORD=password123 \
        postgres:12.1
```

You can also add the `-d` flag to run it in background. And also add [restart policy](https://docs.docker.com/config/containers/start-containers-automatically/#use-a-restart-policy) if needed.

### run using docker-compose
See provided [docker-compose.yml](docker-compose.yml).

Run using:

```
docker-compose up
```

The `-d` flag can be also applied here.

## Test it
After running the database by one of the two provided ways. You have fully working PostgreSQL database ready for use.

If you need different versions or another instance just start another container.
