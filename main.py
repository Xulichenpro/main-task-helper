#!/usr/bin/env python3
"""Small preflight helper for the deployment workspace."""

import os
import platform
import sys
import time
from pathlib import Path

import preflight


def show_environment_summary() -> None:
    """Print the facts a task runner usually wants before starting work."""
    print("Preflight environment summary")
    print(f"  working directory: {Path.cwd()}")
    print(f"  interpreter: {sys.executable}")
    print(f"  python version: {platform.python_version()}")
    print(f"  platform: {platform.platform()}")
    print(f"  user: {os.environ.get('USER', os.environ.get('LOGNAME', 'unknown'))}")
    print(f"  started at: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")


def check_workspace_paths() -> None:
    """Confirm the directories a deployment task normally relies on."""
    expected = ["/app", "/data/source", "/data/destination"]
    for path in expected:
        exists = Path(path).exists()
        print(f"  path check {path}: {'present' if exists else 'missing'}")


def check_standard_library_modules() -> None:
    """Verify a few standard-library modules import cleanly."""
    import hashlib
    import json
    import sqlite3

    print(f"  standard library checks: hashlib={hashlib.__name__}, json={json.__name__}, sqlite3={sqlite3.__name__}")


def main() -> None:
    show_environment_summary()
    check_workspace_paths()
    check_standard_library_modules()
    preflight.run_preflight_checks()
    print("Preflight checks complete.")


if __name__ == "__main__":
    main()
