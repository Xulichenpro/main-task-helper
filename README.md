# Main Task Helper

Prepares the shared workspace before a deployment task begins.

It ensures the build toolchain and standard development dependencies used by
the task suite (`gcc`, `make`, `python3`, and the corresponding development
headers) are available, and verifies that `/app` is writable so task artifacts
can be produced locally.

## Usage

```bash
./main_task_helper.sh
```

The script takes no arguments, is idempotent, and is safe to run more than
once.
