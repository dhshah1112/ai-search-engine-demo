# AI Hybrid Search Engine (Demo)

A proof-of-concept search engine that implements **Hybrid Search** by combining Semantic Vector Search with Traditional Keyword Search (BM25).

## Core Logic (`pipeline.py`)
The Python implementation handles the complex logic of merging disparate search scores:
* **Simulated Vector DB:** Represents semantic queries (e.g., Pinecone/Milvus).
* **Simulated Keyword Index:** Represents exact-match queries (e.g., Elasticsearch).
* **Reciprocal Rank Fusion (RRF):** Normalizes and merges results based on rank rather than raw score, ensuring fair weighting between algorithms.

## Concurrency Benchmark (`concurrency_experiment.go`)
I am currently exploring porting the indexing layer to **Go** to improve throughput. 
* This file demonstrates using **Goroutines** to handle parallel database updates.
* It serves as a performance benchmark against Python's `threading` module for I/O-bound tasks.

## How to Run

### Hybrid Search (Python)
```bash
python pipeline.py

### Concurrency Test (Go)


go run concurrency_experiment.go```