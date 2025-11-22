from fastapi import APIRouter, Security
from fastapi import UploadFile, File
from lantern_api.services import document_service
from lantern_api.library.dependencies import get_api_key
from lantern_api.services import basic_rag_service
import os

router = APIRouter(dependencies=[Security(get_api_key)])

@router.post("/")
async def create_document(
    file: UploadFile = File(...)
):
    # Save document to disk using the document service
    content = await document_service.save_document(file)

    # Process the document content into rag
    RAG_METHOD = os.environ.get("RAG_METHOD", "basic")
    if RAG_METHOD == "basic":
        await basic_rag_service.ingest_document_content(content)
    else:
        raise ValueError(f"Unsupported RAG method: {RAG_METHOD}")

    return {"message": "Document created"}