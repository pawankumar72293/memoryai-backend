# MemoryAI Backend

AI-powered memory cloning backend built with FastAPI, RAG, Qdrant, Gemini AI, WebSockets, and WhatsApp chat intelligence.

This backend allows users to upload WhatsApp chat exports, train AI personas, and chat with emotionally contextual AI personalities in realtime.

---

# Features

## Authentication

- JWT Authentication
- User Registration/Login
- Protected APIs
- Token-based authorization

---

## Persona System

- Create AI personas
- Relationship-based personality modeling
- Persona memory training

---

## WhatsApp Intelligence

- Upload WhatsApp ZIP exports
- Parse WhatsApp chats
- Store structured messages
- AI memory extraction

---

## AI & RAG

- Sentence Transformers embeddings
- Vector search with Qdrant
- Retrieval Augmented Generation (RAG)
- Gemini AI integration
- Context-aware AI responses

---

## Chat System

- REST chat APIs
- Realtime WebSocket chat
- Streaming-ready architecture
- Conversation history
- AI memory context

---

## Backend Architecture

- FastAPI
- SQLAlchemy
- MySQL
- Qdrant
- WebSockets
- Modular service architecture
- Middleware support
- Logging system
- Rate limiting

---

# Tech Stack

- FastAPI
- Python
- SQLAlchemy
- MySQL
- Qdrant
- Sentence Transformers
- Gemini AI
- WebSockets
- JWT
- FAISS/Qdrant Vector Search

---

# Project Structure

```bash
memoryai-backend/
│
├── api/
├── core/
├── database/
├── dependencies/
├── middleware/
├── models/
├── repositories/
├── schemas/
├── services/
├── uploads/
├── workers/
├── main.py
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd memoryai-backend
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
APP_NAME=MemoryAI

DB_HOST=localhost
DB_PORT=3306
DB_NAME=memoryai
DB_USER=root
DB_PASSWORD=

JWT_SECRET_KEY=your_secret
JWT_ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

GEMINI_API_KEY=YOUR_GEMINI_KEY
```

---

# Run Backend

```bash
python -m uvicorn main:app --reload
```

Backend URL:

```bash
http://localhost:8000
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

# Main APIs

## Auth

```http
POST /api/v1/auth/register
POST /api/v1/auth/login
```

## Personas

```http
POST /api/v1/personas
POST /api/v1/personas/{persona_id}/train
```

## Uploads

```http
POST /api/v1/uploads/whatsapp
```

## Chat

```http
POST /api/v1/chat/message
GET /api/v1/chat/history/{persona_id}
```

## WebSocket

```http
ws://localhost:8000/api/v1/websocket/chat/{persona_id}
```

---

# AI Workflow

```text
WhatsApp ZIP Upload
        ↓
Chat Parsing
        ↓
Message Storage
        ↓
Embeddings Generation
        ↓
Qdrant Vector Storage
        ↓
RAG Retrieval
        ↓
Gemini AI Response
        ↓
Realtime Chat
```

---

# Current Status

- Backend MVP Complete
- Frontend Integration Ready
- Deployment Ready
- Realtime AI Chat Working

---

# Future Improvements

- Redis Integration
- Celery Workers
- Docker Compose
- Voice Cloning
- Long-Term Memory
- Emotion Detection
- AI Analytics
- Multi-Persona Support

---

# License

MIT License