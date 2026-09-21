"""Simpele eval-harness: is het antwoord echt gegrond in de context, of verzint
het model iets? Gebruik dit op elke RAG-pipeline vóór je 'm aan een klant laat zien.
"""

from __future__ import annotations

import os

import anthropic


def check_groundedness(
    answer: str,
    context_chunks: list[str],
    client: anthropic.Anthropic | None = None,
) -> dict:
    """Laat een tweede, losse LLM-call beoordelen of het antwoord wordt gedekt door
    de context. Simpel, maar effectiever dan zelf visueel controleren bij veel cases.
    """
    client = client or anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    context = "\n\n---\n\n".join(context_chunks)

    prompt = (
        "Beoordeel of het ANTWOORD volledig wordt ondersteund door de CONTEXT. "
        "Antwoord met exact één van: GEGROND, DEELS_GEGROND, NIET_GEGROND, "
        "gevolgd door een toelichting van 1 zin.\n\n"
        f"CONTEXT:\n{context}\n\nANTWOORD:\n{answer}"
    )

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    verdict_text = response.content[0].text
    verdict = verdict_text.split(",")[0].split()[0].strip()

    return {"verdict": verdict, "toelichting": verdict_text}


def run_eval_set(cases: list[dict]) -> None:
    """cases: [{"answer": ..., "context_chunks": [...]}]

    Gebruik dit op een setje van 5-10 representatieve vragen, niet op één losse case —
    dat is wat een eval-harness onderscheidt van handmatig testen.
    """
    results = [check_groundedness(c["answer"], c["context_chunks"]) for c in cases]
    n_gegrond = sum(1 for r in results if r["verdict"] == "GEGROND")
    print(f"{n_gegrond}/{len(results)} volledig gegrond.")
    for i, r in enumerate(results):
        if r["verdict"] != "GEGROND":
            print(f"  case {i}: {r['verdict']} — {r['toelichting']}")


if __name__ == "__main__":
    print("Importeer check_groundedness(answer, context_chunks) of run_eval_set(cases).")
