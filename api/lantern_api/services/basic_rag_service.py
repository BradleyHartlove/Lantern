import os

# Configuration for basic RAG service
BASIC_RAG_CHUNKING_METHOD = os.environ.get("BASIC_RAG_CHUNKING_METHOD", "token")
BASIC_RAG_CHUNKING_TOKEN_COUNT = int(os.environ.get("BASIC_RAG_CHUNKING_TOKEN_COUNT", 300))
BASIC_RAG_CHUNKING_TOKEN_OVERLAP_COUNT = int(os.environ.get("BASIC_RAG_CHUNKING_TOKEN_OVERLAP_COUNT", 30))

def ingest_document_content(content: str):
    # Placeholder for processing document content into RAG
    pass