from fastapi import APIRouter, Security
from fastapi import UploadFile, File
from lantern_api.services import document_service
from lantern_api.library.dependencies import get_api_key

router = APIRouter(dependencies=[Security(get_api_key)])

@router.post("/")
async def create_document(
    file: UploadFile = File(...)
):
    # Save document to disk using the document service
    await document_service.save_document(file)
    return {"message": "Document created"}