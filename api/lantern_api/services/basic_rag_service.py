import os
from lantern_api.library.chunking import chunk_text
from lantern_api.services.embedding_service import generate_embedding
import logging

logger = logging.getLogger(__name__)

# Configuration for basic RAG service
BASIC_RAG_CHUNKING_METHOD = os.environ.get("BASIC_RAG_CHUNKING_METHOD", "token")
BASIC_RAG_CHUNKING_TOKEN_COUNT = int(os.environ.get("BASIC_RAG_CHUNKING_TOKEN_COUNT", 300))
BASIC_RAG_CHUNKING_TOKEN_OVERLAP_COUNT = int(os.environ.get("BASIC_RAG_CHUNKING_TOKEN_OVERLAP_COUNT", 30))

async def ingest_document_content(content: str):
    # Start by creating chunks based on the configured method
    chunks = []
    if BASIC_RAG_CHUNKING_METHOD == "token":
        chunks = chunk_text(
            text=content,
            max_tokens=BASIC_RAG_CHUNKING_TOKEN_COUNT,
            token_overlap=BASIC_RAG_CHUNKING_TOKEN_OVERLAP_COUNT
        )

    embeddings = [
        await generate_embedding(chunk) for chunk in chunks
    ]

    logger.error(f"Ingested document content into {len(chunks)} chunks with embeddings.")
    logger.error(f"EMBEDDING SIZE: {len(embeddings[0]) if embeddings else 0}")