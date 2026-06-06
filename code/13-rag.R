# 13-rag.R
# Deck 03: Prompt engineering and RAG (RAG)
# Goal: build a dynamic RAG system over the R for Data Science book. Chunk the
# text, compute embeddings with ragnar, and expose retrieval as a tool.

library(ellmer)
library(ragnar)

# TODO: ingest documents and build an embedding store with ragnar
# TODO: register a retrieval tool against the chat object
