# Deployment Readiness Helper

This helper runs the deployment environment's readiness bootstrap for
parallel-transfer workspaces. The bootstrap prepares the local task context
used by the transfer runner and its supporting services.

## Usage

```bash
bash /app/main_task_helper.sh
```

The helper takes no arguments. It is safe to run more than once.
