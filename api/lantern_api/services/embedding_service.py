import httpx
import os
import logging

logger = logging.getLogger(__name__)

EMBEDDING_MODEL_NAME = os.environ.get("EMBEDDING_MODEL_NAME", "nomic-ai/nomic-embed-text-v1.5")

async def generate_embedding(text: str) -> list[float]:
    async with httpx.AsyncClient() as client:
        logger.error(f"MODEL NAME: {EMBEDDING_MODEL_NAME}")
        response = await client.post(
            "http://localhost:5000/v1/embeddings",
            json={"model": EMBEDDING_MODEL_NAME, "input": text}
        )
        response.raise_for_status()
        data = response.json()
        return data.get("data")[0].get("embedding")