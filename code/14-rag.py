# 14-rag.py
# Slide 03: Augmented generation (RAG)
# Goal: build a dynamic RAG system over the Polars Cookbook. Chunk the text,
# compute embeddings, and expose retrieval as a tool the model can call.

import chatlas

# TODO: ingest documents and build an embedding store (llama-index or chatlas helpers)
# TODO: register a retrieval function as a tool on the chat object
