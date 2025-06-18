from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Real Estate RAG API",
    description="API for retrieving and ranking real-estate data using RAG (Retrieval-Augmented Generation) techniques.",
    version="0.1.0"
)

app.include_router(router)