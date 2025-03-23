# Hatchet Starter

> Minimal containerized [Hatchet](https://hatchet.run) starter for Python

## Quick start

```sh
docker compose up --build --watch

## or, demonstrate horizontally scaling Hatchet (up to 2) and/or worker (limit depends on hardware)
docker compose up --build --watch --scale hatchet=2 --scale worker=3

## cleanup
docker compose down --volumes
```

## Links

- Hatchet web console: [localhost:48879](http://localhost:48879/) or [localhost:48880](http://localhost:48880/) (Docker Compose seems to grab one nondeterministically)
  - username: `founders@example.com`
  - password: `Admin123!!`
