# syntax=docker/dockerfile:1

ARG HATCHET_VERSION_TAG=v0.57.1

FROM ghcr.io/hatchet-dev/hatchet/hatchet-lite:${HATCHET_VERSION_TAG} AS hatchet-lite
FROM ghcr.io/hatchet-dev/hatchet/hatchet-api:${HATCHET_VERSION_TAG} AS hatchet-api
FROM ghcr.io/hatchet-dev/hatchet/hatchet-engine:${HATCHET_VERSION_TAG} AS hatchet-engine

## https://github.com/hatchet-dev/hatchet/blob/v0.55.21/build/package/servers.dockerfile#L62-L82
## https://github.com/hatchet-dev/hatchet/blob/v0.55.21/build/package/lite.dockerfile#L24-L48
FROM alpine AS base

WORKDIR /opt/hatchet

RUN apk update && apk add --no-cache gcc musl-dev openssl bash ca-certificates curl postgresql-client

COPY --from=hatchet-lite --link /hatchet-admin /hatchet-lite /hatchet-migrate ./
COPY --from=hatchet-api --link /hatchet/hatchet-api ./
COPY --from=hatchet-engine --link /hatchet/hatchet-engine ./

RUN ["/usr/bin/env", "bash", "-e", "-c", "ln -s /opt/hatchet/hatchet-* /usr/local/bin/"]

COPY --from=hatchet-lite --link /static-assets /static-assets
COPY docker/entrypoint /entrypoint
COPY config ./config

ARG LITE_FRONTEND_PORT='8081'
ARG LITE_RUNTIME_PORT='8888'
ARG SERVER_GRPC_PORT='7070'
ARG SERVER_PORT='8080'

ENV LITE_FRONTEND_PORT=${LITE_FRONTEND_PORT} \
    LITE_RUNTIME_PORT=${LITE_RUNTIME_PORT} \
    LITE_STATIC_ASSET_DIR='/static-assets' \
    SERVER_GRPC_BIND_ADDRESS='0.0.0.0' \
    SERVER_GRPC_PORT=${SERVER_GRPC_PORT} \
    SERVER_PORT=${SERVER_PORT} \
    SERVER_DEFAULT_ENGINE_VERSION=V1

EXPOSE ${LITE_FRONTEND_PORT} ${LITE_RUNTIME_PORT} ${SERVER_GRPC_PORT} ${SERVER_PORT}

ENTRYPOINT ["/entrypoint"]
CMD ["hatchet-lite", "--config", "/opt/hatchet/config"]

FROM base AS dev

COPY docker/init-local.sh /init-local.sh

HEALTHCHECK --interval=30s --timeout=2s --start-period=15s --start-interval=3s --retries=3 \
  CMD (curl --fail localhost:8080/api/ready && curl --fail localhost:8733/ready) || exit 1
