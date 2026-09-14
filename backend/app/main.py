from fastapi import FastAPI
from backend.app.api.routes.query import router as query_router
from backend.app.utils.logging_config import setup_logging

setup_logging()

app = FastAPI(
    title="Alzheimer's Medical RAG API",
    version="1.0.0"
)

app.include_router(query_router, prefix="/api", tags=["RAG Query"])

@app.get("/")
def root():
    return {"message": "Welcome to the Alzheimer's RAG Assistant API!"}