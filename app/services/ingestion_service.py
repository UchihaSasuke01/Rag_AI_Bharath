from app.loaders.pdf_loader import load_and_split_pdf
from app.services.vector_store import get_vector_store

async def ingest_pdf(file_path: str, scheme_id: str, version: str):

    docs = load_and_split_pdf(file_path)

    for doc in docs:
        doc.metadata["schemeId"] = scheme_id
        doc.metadata["version"] = version

    vector_store = get_vector_store()
    vector_store.add_documents(docs)
