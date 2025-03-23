#!/usr/bin/env bash
set -eo pipefail

: ${X_HATCHET_CLIENT_SECRETS_DIR?"X_HATCHET_CLIENT_SECRETS_DIR must be set"}

mkdir -p "${X_HATCHET_CLIENT_SECRETS_DIR}"

hatchet_client_token_file="${X_HATCHET_CLIENT_SECRETS_DIR}/hatchet_client_token"

if ! [ -f "${hatchet_client_token_file}" ] || [ -s "${hatchet_client_token_file}" ]; then
  ## adapted from https://github.com/hatchet-dev/hatchet/blob/v0.53.14/frontend/docs/pages/self-hosting/hatchet-lite.mdx?plain=1#L142-L143
  ten_years_in_hours="$(expr 10 '*' 365 '*' 24)"
  hatchet-admin --config /opt/hatchet/config \
    token create \
      --tenant-id 00000000-0000-0000-0000-000000000000 --expiresIn "${ten_years_in_hours}h0m0s" \
    | tee "${hatchet_client_token_file}"
fi
