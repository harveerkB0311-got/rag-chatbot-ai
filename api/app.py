import sys
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel


BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from chatbot import RAGChatbot


app = FastAPI(title="RAG Chatbot AI API")

chatbot = RAGChatbot()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG Chatbot AI API is running"}


@app.post("/chat")
def chat(request: ChatRequest):
    return chatbot.answer_question(request.question)
