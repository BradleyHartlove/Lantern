import os
import sys

# Ensure the package parent directory is on sys.path so the package
# `lantern_api` can be imported whether this file is executed from the
# package directory or the repository root.
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lantern_api.app import create_app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, host="localhost", port=8000)