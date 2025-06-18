# Personalized Real Estate RAG Recommender

A production-ready system that matches homebuyers with personalized property listings using Retrieval-Augmented Generation (RAG), vector embeddings, and FastAPI.

## Features

- Hybrid retrieval: FAISS vector search + cross-encoder re-ranking
- Personalized matching based on buyer preferences
- FastAPI backend with Redis cache and Prometheus monitoring
- Dockerized, autoscalable deployment

## Roadmap

- [x] Project scaffolding
- [ ] Data ingestion + embedding
- [ ] FAISS vector index
- [ ] Cross-encoder re-ranker
- [ ] FastAPI + Redis cache
- [ ] Prometheus / Grafana metrics
- [ ] Docker & CI/CD deployment


## Project Structure
```
app/
├── api/ # FastAPI endpoints
├── models/ # Pydantic models
├── utils/ # FAISS, embeddings, re-ranking
└── data/ # Raw and processed data
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Then visit:

API root: http://localhost:8000/

Docs UI: http://localhost:8000/docs
