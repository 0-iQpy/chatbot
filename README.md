# Local Customer Support Chatbot

## Overview

This project is a **local-hosted customer support chatbot** that answers user FAQs and support questions based on ingested documents (e.g., PDFs, manuals, policies). It uses **FastAPI** for the backend, **Supabase Vector DB** for knowledge storage, and optionally **Ollama (Llama 3.2:1B)** for local inference.

The chatbot is designed for modularity, allowing easy migration to a cloud environment later.

---

## Features

* Document ingestion and embedding (PDF, Markdown)
* Vector-based semantic search using Supabase
* Real-time text-based chat endpoint
* Logging for ingestion and chat sessions
* JWT-based authentication (admin/user)

---

## How It Works

### 1. Document Ingestion

Admin uploads documents through `/ingest` endpoint.

* The text is extracted and chunked (~500 tokens per chunk).
* Each chunk is embedded using the chosen embedding model (Ollama/OpenAI).
* Embeddings and metadata are stored in Supabase Vector DB.

### 2. Query Handling

User sends a question to `/chat` endpoint.

* The system embeds the query.
* Retrieves top-k most similar document chunks from the vector database.
* Generates a context-aware answer using the LLM.
* Returns the answer with source references.

### 3. Logging

All ingestion and chat activities are logged locally for debugging and evaluation.

---

## Quick Start

### Prerequisites

* Python 3.11+
* FastAPI, Uvicorn
* Supabase account (or local Docker setup)
* Ollama installed with model: `llama3.2:1b`

### Environment Variables (.env)

```
SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_api_key>

it depends on the method you want to use to connect to your database
```

### Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open your browser at `http://127.0.0.1:8000/docs`.

### Test Ingestion

```bash
curl -X POST "http://127.0.0.1:8000/ingest" \
-F "file=@sampleFAQs.pdf" \
-H "Authorization: Bearer <your_admin_token>"
```

### Test Chat

```bash
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{"query": "How to reset my password?"}'
```

---

## Architecture

* **FastAPI**: Backend REST API
* **Ollama / OpenAI**: Embedding + Response generation
* **Supabase Vector**: Vector similarity search
* **PostgreSQL (Supabase)**: Metadata + auth
* **Local Logs**: CSV or JSON logs for ingestion and chat history

---

## Next Steps

* Add feedback endpoint (`/feedback`) for training data collection.
* Build minimal chat UI (HTML/JS).
* Add role-based access control for multi-user setups.

---
