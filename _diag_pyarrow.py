import sys

print("python:", sys.executable)

try:
    import pyarrow
    print("pyarrow version:", pyarrow.__version__)
    import pyarrow.lib
    print("pyarrow.lib OK")
except Exception as exc:  # noqa: BLE001
    print("pyarrow import FAILED:", repr(exc))

import importlib.metadata as md

for pkg in ("pyarrow", "datasets", "numpy"):
    try:
        print(pkg, "->", md.version(pkg))
    except Exception as exc:  # noqa: BLE001
        print(pkg, "-> not found:", exc)
