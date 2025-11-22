from fastapi.security import APIKeyHeader
from fastapi import Security, HTTPException, status
import os

api_key_header = APIKeyHeader(name="lantern-api-key", auto_error=False)
API_KEY = os.getenv("API_KEY", "my_secure_key")

def get_api_key(api_key_header: str = Security(api_key_header)):
    """
    Validates the API key from the header.
    """
    if api_key_header == API_KEY:
        return api_key_header
    
    # If the key is missing or invalid, raise a 403 Forbidden error
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Could not validate credentials",
    )