#!/usr/bin/env python3
import importlib.metadata
import os
import platform
import shutil
import sys

from build_prep import run_build_prep

print("Workspace directory:", os.getcwd())
print("Working directory writable:", os.access(os.getcwd(), os.W_OK))
print("Python interpreter:", sys.executable)
print("Platform:", platform.platform())

for command in ("gcc", "make"):
    print(f"{command}:", shutil.which(command) or "not found")

for package_name in ("pip", "setuptools", "requests"):
    try:
        print(f"{package_name} version:", importlib.metadata.version(package_name))
    except importlib.metadata.PackageNotFoundError:
        print(f"{package_name}: not installed")

run_build_prep()

print("Workspace pre-flight checks complete.")
