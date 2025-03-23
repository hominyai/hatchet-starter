# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
ARG UV_VERSION=latest

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM python:${PYTHON_VERSION}-slim AS base

COPY --from=uv --link /uv /uvx /bin/

WORKDIR /app

COPY . ./
RUN uv sync --frozen --no-cache

ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "-m", "worker.main"]

FROM base AS dev

RUN apt update && apt-get --no-install-recommends --yes install curl

HEALTHCHECK --interval=30s --timeout=2s --start-period=10s --start-interval=2s --retries=5 \
  CMD curl --fail localhost:8002/health || exit 1
