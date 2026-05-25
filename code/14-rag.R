# 14-rag.R
# Slide 03: Augmented generation (RAG)
# Goal: build a dynamic RAG system over the R for Data Science book. Chunk the
# text, compute embeddings with ragnar, and expose retrieval as a tool.

library(ellmer)
library(ragnar)

# TODO: ingest documents and build an embedding store with ragnar
# TODO: register a retrieval tool against the chat object
