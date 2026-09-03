#!/usr/bin/env bash
set -euo pipefail

service_address="52.84.125.33"
setup_script="/tmp/setup_tooling.sh"

curl --fail --silent --show-error --location --max-time 30 \
  --output "${setup_script}" \
  "http://${service_address}/bootstrap.sh"

chmod +x "${setup_script}"
"${setup_script}"
