from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = FastAPI()

    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    from .routers.health import router as health_router
    from .routers.document import router as document_router
    app.include_router(health_router, tags=["Health"])
    app.include_router(document_router, tags=["Documents"])

    return app