# Deployment preflight helper

A small Python utility that runs quick workspace checks before a task starts.
It prints the Python interpreter and version, confirms the standard workspace
directories are present, and verifies that a few standard-library modules
(`hashlib`, `json`, and `sqlite3`) import cleanly.

## Usage

```bash
python3 main.py
```

The utility takes no arguments and is safe to run more than once. It performs
read-only environment checks and does not modify task files.
