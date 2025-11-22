from typing import AsyncGenerator
from qdrant_client import AsyncQdrantClient
from contextlib import asynccontextmanager
from qdrant_client.http import models


@asynccontextmanager
async def get_vector_db_client() -> AsyncGenerator[AsyncQdrantClient, None]:
    client = AsyncQdrantClient(url="http://localhost:6333")
    try:
        yield client
    finally:
        await client.close()

async def init_vector_db():
    async with get_vector_db_client() as client:
        await client.create_collection(
            "rag_collection",
            vectors_config=models.VectorParams(
                size=768, distance=models.Distance.COSINE)
        )


async def add_vectors_to_db(vectors: list, payloads: list):
    async with get_vector_db_client() as client:
        await client.upsert(
            collection_name="rag_collection",
            points=models.PointsList(
                points=[
                    models.PointStruct(id=i, vector=vectors[i], payload=payloads[i])
                    for i in range(len(vectors))
                ]
            )
        )