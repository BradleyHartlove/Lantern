from fastapi import APIRouter, Security
from lantern_api.library.dependencies import get_api_key

router = APIRouter(dependencies=[Security(get_api_key)])

@router.post("/")
def create_document():
    return {"message": "Document created"}