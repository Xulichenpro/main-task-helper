# Main task helper

`main_task_helper.sh` prepares the workspace for tasks that use a C build-and-check cycle with `gcc`, `make`, and standard system headers.

## Usage

```bash
./main_task_helper.sh
```

The helper takes no arguments. It is safe to run again, and a nonzero exit means the workspace is not ready for the build-and-check cycle.
