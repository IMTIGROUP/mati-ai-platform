
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="MATI AI API",
    description="MATI AI Platform Backend",
    version="0.1.0"
)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


@app.get("/")
def home():
    return {
        "name": "MATI AI",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/api/v1/chat")
def chat(request: ChatRequest):
    return {
        "success": True,
        "mode": "mock",
        "message": request.message,
        "reply": (
            "Welcome to MATI AI! "
            "Your backend is working. "
            "AI model integration is coming next."
        )
    }
