# Main Task Helper

A small workspace pre-flight utility used by the deployment tasks.

It checks the local build environment before a task starts:

- confirms the working directory is mounted and writable
- reports the Python interpreter and installed package versions
- verifies that `gcc` and `make` are available
- runs the build-preparation routine so the standard build toolchain is present and ready

## Usage

```sh
python3 main.py
```

The utility takes no arguments and is safe to run more than once.
