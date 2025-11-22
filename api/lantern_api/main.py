import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lantern_api.app import create_app

if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, host="localhost", port=8000)