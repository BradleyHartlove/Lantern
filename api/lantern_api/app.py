from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    from .services.document_service import init_document_storage
    try:
        init_document_storage()
    except Exception as e:
        logger.error(f"Error during document storage initialization: {e}")
        raise e
    yield


def create_app():
    app = FastAPI(lifespan=lifespan)

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
    from .routers.documents_router import router as document_router
    app.include_router(health_router, tags=["Health"])
    app.include_router(document_router, tags=["Documents"])

    return app