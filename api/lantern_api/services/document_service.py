import os
import aiofiles
import logging
from fastapi import UploadFile

logger = logging.getLogger(__name__)

DOCUMENT_STORAGE_LOCATION = os.environ.get("DOCUMENT_STORAGE_LOCATION", "/opt/documents")

def init_document_storage():
    try:
        os.makedirs(DOCUMENT_STORAGE_LOCATION, exist_ok=True)
        logging.info(f"Document storage initialized at {DOCUMENT_STORAGE_LOCATION}")
    except Exception as e:
        raise RuntimeError(f"Failed to create document storage directory: {e}")

async def save_document(file: UploadFile) -> str:
    file_name = file.filename
    content = file.file.read()  # TODO: Implement non text files handling
    file_path = os.path.join(DOCUMENT_STORAGE_LOCATION, file_name)
    try:
        async with aiofiles.open(file_path, "wb") as f:
            await f.write(content)
        logging.info(f"Document saved: {file_path}")
        return content
    except Exception as e:
        raise RuntimeError(f"Failed to save document {file_name}: {e}")