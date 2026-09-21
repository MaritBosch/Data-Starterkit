"""Minimale RAG-pipeline template.

Volgorde uit praktijklog: test eerst het kale model zonder retrieval (baseline) ->
chunk + test retrieval APART van generatie -> voeg pas dan de LLM-call toe, met de
instructie om zich te beperken tot de opgehaalde context.

Retrieval hier is TF-IDF (geen extra API-key nodig, makkelijk lokaal te testen).
Vervang dit voor een echt project door een neurale embedding (bv. Vertex AI's
text-embedding-model, of de Voyage/OpenAI embeddings-API) — de rest van de flow
blijft identiek.
"""

from __future__ import annotations

import os

import anthropic
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """Simpele vaste-lengte chunking met overlap. Niet te groot, niet te klein —
    test met een paar chunk_size-waarden wat voor jouw documenten werkt."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


class Retriever:
    """TF-IDF-retriever — test dit ALTIJD los: geeft retrieve() de juiste passage
    terug, los van wat de LLM er straks mee doet?"""

    def __init__(self, chunks: list[str]):
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.matrix).flatten()
        top_idx = scores.argsort()[::-1][:top_k]
        return [self.chunks[i] for i in top_idx]


def generate_answer(query: str, context_chunks: list[str], client: anthropic.Anthropic | None = None) -> str:
    """Genereert een antwoord, expliciet beperkt tot de opgehaalde context.

    Test bewust ook een vraag waar het antwoord NIET in de context staat — het
    model moet dan 'weet ik niet' zeggen, niet iets verzinnen.
    """
    client = client or anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    context = "\n\n---\n\n".join(context_chunks)

    prompt = (
        "Beantwoord de vraag UITSLUITEND op basis van de onderstaande context. "
        "Als het antwoord niet in de context staat, zeg dat expliciet — verzin niets.\n\n"
        f"CONTEXT:\n{context}\n\nVRAAG: {query}"
    )

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def rag_answer(query: str, retriever: Retriever, top_k: int = 3) -> str:
    context_chunks = retriever.retrieve(query, top_k=top_k)
    return generate_answer(query, context_chunks)


if __name__ == "__main__":
    print(
        "1. chunk_text(document) -> chunks\n"
        "2. Retriever(chunks) -> test retriever.retrieve(query) APART\n"
        "3. pas dan rag_answer(query, retriever) aanroepen"
    )
