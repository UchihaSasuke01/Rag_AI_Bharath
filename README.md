# RAG AI Bharath

A Retrieval-Augmented Generation (RAG) API built with FastAPI, LangChain, and Qdrant vector database. This application allows you to ingest PDF documents and query them using AI-powered semantic search.

## Features

- **PDF Ingestion**: Upload and process PDF documents with automatic chunking and embedding
- **Vector Database**: Uses Qdrant for efficient semantic search with text-embedding-3-large embeddings
- **RAG Chain**: Leverages LangChain and OpenRouter LLM for intelligent question answering
- **RESTful API**: Simple and intuitive FastAPI endpoints for ingestion and querying
- **Scalable Architecture**: Modular design for easy extension and customization

## Tech Stack

- **Framework**: FastAPI 
- **LLM & Embeddings**: OpenRouter API + OpenAI Embeddings
- **Vector Database**: Qdrant
- **LangChain Ecosystem**:
  - langchain (core orchestration)
  - langchain-core (base classes)
  - langchain-community (integrations)
  - langchain-openai (OpenAI integration)
  - langchain-qdrant (Qdrant integration)
  - langchain-text-splitters (document chunking)
- **Server**: Uvicorn
- **Config Management**: python-dotenv, Pydantic

## Project Structure

```
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── app/                               # Main application directory
│   ├── main.py                       # FastAPI app initialization
│   ├── api/
│   │   ├── ingest_routes.py         # PDF ingestion endpoints
│   │   └── rag_routes.py            # RAG query endpoints
│   ├── core/
│   │   └── config.py                # Configuration and settings
│   ├── loaders/
│   │   └── pdf_loader.py            # PDF processing logic
│   └── services/
│       ├── ingestion_service.py     # PDF ingestion logic
│       ├── rag_chain.py             # RAG chain orchestration
│       └── vector_store.py          # Qdrant vector store client
└── scripts/
    └── create_dummy_pdf.py          # Utility for generating test PDFs
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Rag_AI_Bharath
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file** in the project root
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   OPENROUTER_MODEL=your_preferred_model
   OPENAI_EMBED_MODEL=text-embedding-3-large
   QDRANT_URL=http://localhost:6333
   QDRANT_COLLECTION=documents
   ```

## Prerequisites

### Qdrant Vector Database

Start Qdrant using Docker:

```bash
docker run -p 6333:6333 -p 6334:6334 \
  -e QDRANT__S3_CONFIG__ENABLED=false \
  qdrant/qdrant:latest
```

## Usage

### Start the Server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### 1. Health Check
```bash
GET /health
```

Response:
```json
{
  "status": "ok"
}
```

#### 2. Ingest PDF Document
```bash
POST /admin/ingest
```

**Parameters**:
- `file` (FormData): PDF file to upload
- `scheme_id` (query): Identifier for the document scheme
- `version` (query): Version of the document

**Example**:
```bash
curl -X POST "http://localhost:8000/admin/ingest" \
  -F "file=@document.pdf" \
  -F "scheme_id=scheme_001" \
  -F "version=v1"
```

**Response**:
```json
{
  "status": "ingested"
}
```

#### 3. Ask Question (RAG Query)
```bash
POST /rag/ask
```

**Request Body**:
```json
{
  "question": "What does the document say about topic X?"
}
```

**Example**:
```bash
curl -X POST "http://localhost:8000/rag/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the main topic?"}'
```

**Response**:
```json
{
  "answer": "The document discusses..."
}
```

## Configuration

Settings are managed in [app/core/config.py](app/core/config.py) using Pydantic's BaseSettings:

| Variable | Description | Example |
|----------|-------------|---------|
| `OPENROUTER_API_KEY` | OpenRouter API authentication key | sk-... |
| `OPENROUTER_MODEL` | LLM model to use via OpenRouter | openai/gpt-4-turbo |
| `OPENAI_EMBED_MODEL` | Embedding model | text-embedding-3-large |
| `QDRANT_URL` | Qdrant database URL | http://localhost:6333 |
| `QDRANT_COLLECTION` | Vector collection name | documents |

## Development

### Generate Test PDFs

```bash
python scripts/create_dummy_pdf.py
```

### Directory Layout

- **loaders/**: PDF loading and processing logic
- **services/**: Business logic for ingestion and RAG operations
- **api/**: Route definitions for REST endpoints
- **core/**: Configuration and shared utilities

## How It Works

1. **PDF Ingestion**:
   - PDF is uploaded and temporarily stored
   - Document is split into chunks using LangChain text splitters
   - Chunks are embedded using OpenAI's text-embedding-3-large model
   - Embeddings are stored in Qdrant vector database

2. **RAG Query**:
   - User question is received via API
   - Similar documents/chunks are retrieved from Qdrant using semantic similarity
   - Retrieved context is combined with the question
   - OpenRouter LLM generates answer based on the context

## API Documentation

Once the server is running, please refer:
- **Swagger UI**: http://localhost:8000/docs