from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from app.core.config import settings

VECTOR_SIZE = 3072  # text-embedding-3-large dimension


def get_vector_store():

    client = QdrantClient(url=settings.QDRANT_URL)

    # Ensure collection exists
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if settings.QDRANT_COLLECTION not in names:
        client.create_collection(
            collection_name=settings.QDRANT_COLLECTION,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )

    embeddings = OpenAIEmbeddings(
        model=settings.OPENAI_EMBED_MODEL,
        openai_api_key=settings.OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
    )

    return QdrantVectorStore(
        client=client,
        collection_name=settings.QDRANT_COLLECTION,
        embedding=embeddings,
    )
