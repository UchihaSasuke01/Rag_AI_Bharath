from fastapi import APIRouter
from app.services.rag_chain import get_rag_chain

router = APIRouter()


@router.post("/ask")
async def ask_question(payload: dict):

    question = payload.get("question")

    chain = get_rag_chain()

    result = chain.invoke(question)

    return {"answer": result}
