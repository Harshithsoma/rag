# Retrieval-Augmented Generation (RAG) System – Open Source Implementation

This repository contains a complete implementation of a Retrieval-Augmented Generation (RAG) pipeline built using open source tools. It provides a modular setup for building intelligent, context-aware AI applications powered by local embeddings, a vector database, and a retrieval workflow designed for domain-specific knowledge systems.

---

## Overview

This project demonstrates how to:

- Process and embed textual data locally
- Store and index embeddings using PostgreSQL with pgvector
- Retrieve relevant context for a query
- Use a local LLM to generate grounded and accurate responses
- Run everything in an isolated, reproducible development container

---

## Features

### Local Embedding Model

Uses the **Qwen3-Embedding-0.6B** model for generating vector embeddings without external API calls.

### Vector Database

Includes PostgreSQL with the **pgvector** extension for high-performance similarity search.

### Document Ingestion Pipeline

Utilities for:

- text extraction
- chunking
- embedding generation
- metadata + vector storage

### Retrieval Pipeline

Implements the complete RAG workflow:

1. Embed the query
2. Retrieve matching documents
3. Generate a contextual response

### Local LLM Integration

Supports **Ollama** for running lightweight language models fully offline.

### Dev Container Setup

A fully configured VS Code Dev Container including:

- Python environment
- Postgres + pgvector
- Automatic embedding model download
- Helpful CLI utilities

---

## Getting Started

### Clone the repository

```sh
git clone https://github.com/Harshithsoma/rag.git
```

### Open in Dev Container

In VS Code:

1. Open the folder
2. Select **Reopen in Container**

The container automatically sets up:

- all dependencies
- PostgreSQL
- the embedding model
- Python packages

---

## Project Structure

```
/models                 # Embedding model storage
/src                    # Source code for ingestion, embeddings, retrieval
/data                   # Documents or datasets
/db                     # Database initialization, utilities, SQL scripts
notebooks               # Experiments and testing
Dockerfile              # Container image build
devcontainer.json       # VS Code Dev Container configuration
README.md
```

---

## Technology Stack

- Python
- PostgreSQL
- pgvector
- Qwen3 Embedding model
- Ollama for LLM inference
- SQLAlchemy
- NLTK / text preprocessing
- Docker / VS Code Dev Containers

---

## Use Cases

This RAG system can be adapted for:

- AI chatbots grounded in private documents
- Advanced document retrieval systems
- Enterprise search
- Knowledge assistants for teams
- Research Q&A systems
- Offline or local AI experimentation

---

## Roadmap

Planned enhancements include:

- Hybrid search (sparse + dense)
- LLM evaluation utilities
- Web API layer
- Interactive UI for testing queries
- Additional vector models

---

## License

This project is created and maintained independently using open-source components compatible with their respective licenses.
