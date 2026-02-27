from fastapi import APIRouter, UploadFile
import shutil
from app.services.ingestion_service import ingest_pdf

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile, scheme_id: str, version: str):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await ingest_pdf(file_path, scheme_id, version)

    return {"status": "ingested"}
