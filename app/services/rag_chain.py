from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from app.services.vector_store import get_vector_store
from app.core.config import settings


def get_rag_chain():

    # LLM
    llm = ChatOpenAI(
        model=settings.OPENROUTER_MODEL,
        openai_api_key=settings.OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0,
    )

    # Vector store retriever
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    # Prompt
    prompt = ChatPromptTemplate.from_template(
        """
You are an AI assistant helping rural citizens understand government schemes.

Use ONLY the provided context to answer the question clearly and accurately.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""
    )
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
