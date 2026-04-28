# RAG Chatbot AI Project

This is a beginner-friendly Retrieval-Augmented Generation (RAG) chatbot project.  
It answers questions using a custom knowledge base instead of only relying on a general chatbot model.

This project is useful for AI/ML, Backend Python, Automation, and AI Engineer roles.

## What Is RAG?

RAG means Retrieval-Augmented Generation.  
The chatbot first searches relevant documents, then uses those results to generate a helpful answer.

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- TF-IDF Vector Search
- REST API
- Custom Knowledge Base

## Features

- Loads custom business knowledge documents
- Finds the most relevant document using TF-IDF similarity
- Returns chatbot-style answers
- Provides REST API endpoint
- GitHub-ready project structure
- No paid OpenAI API required

## Project Structure

```text
rag-chatbot-ai/
├── api/
│   └── app.py
├── data/
│   └── knowledge_base.txt
├── src/
│   ├── chatbot.py
│   ├── retriever.py
│   └── run_chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Test chatbot in terminal

```bash
python src/run_chatbot.py
```

### 3. Run API

```bash
uvicorn api.app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## API Example

Request:

```json
{
  "question": "What is a loan approval model?"
}
```

Response:

```json
{
  "question": "What is a loan approval model?",
  "answer": "Based on the knowledge base: A loan approval model predicts whether a loan application should be approved or rejected...",
  "source": "A loan approval model predicts whether a loan application should be approved or rejected..."
}
```

