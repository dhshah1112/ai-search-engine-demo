# AI Hybrid Search Engine (Concept Demo)

A small, self-contained demo of **hybrid retrieval** — combining semantic
vector search with keyword search (BM25) and merging the two ranked lists
with **Reciprocal Rank Fusion**.

This is a teaching/illustration repo, not a production system: the vector
and keyword backends are stubbed with fixed results so the fusion logic is
readable in isolation. My production retrieval work (pgvector + HNSW,
BGE-large embeddings, a cross-encoder reranker, and RAGAS-based evaluation)
lives in private company repos.

## Core logic (`pipeline.py`)
- **Stubbed vector backend** — stands in for semantic retrieval; matches on
  meaning ("fruit" → "apple").
- **Stubbed keyword backend** — stands in for BM25/lexical retrieval; catches
  exact tokens like error codes and IDs that embeddings often miss.
- **Reciprocal Rank Fusion** — merges the two lists by *rank* rather than raw
  score: `score = 1 / (k + rank)`, with `k = 60`. Rank-based fusion avoids
  having to calibrate two incompatible score distributions (BM25 scores are
  unbounded, cosine similarity is not), and `k` damps the influence of any
  single top-ranked result.

## Concurrency experiment (`concurrency_experiment.go`)
Exploring whether the indexing layer would benefit from Go. Runs two
I/O-bound indexing tasks concurrently with goroutines and a `WaitGroup`,
and prints wall-clock time against the sequential baseline (~2.5s vs ~5s).
A starting point for a real benchmark, not a rigorous one.

## Running it
```bash
python pipeline.py
go run concurrency_experiment.go
```
