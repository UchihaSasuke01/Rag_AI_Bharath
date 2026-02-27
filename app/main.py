from fastapi import FastAPI
from app.api import rag_routes, ingest_routes

app = FastAPI()

app.include_router(rag_routes.router, prefix="/rag")
app.include_router(ingest_routes.router, prefix="/admin")

@app.get("/health")
def health():
    return {"status": "ok"}
