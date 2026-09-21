# 07 — GenAI & LLM-integratie

- `rag_pipeline_template.py` — minimale RAG-flow: chunk → embed → retrieve → generate,
  als losse functies zodat je retrieval apart kunt testen van generatie (zie de
  voorbeeldaanpak: dat splitsen is de belangrijkste debug-stap).
- `eval_harness_template.py` — simpele groundedness-check: wordt het antwoord echt
  door de opgehaalde context gedekt, of verzint het model iets?

Geschreven tegen de Anthropic SDK (`anthropic`), qua structuur net zo makkelijk om te
zetten naar OpenAI of Vertex AI's Gemini SDK — de flow (chunk/embed/retrieve/generate)
blijft hetzelfde.

## Referentie

Voor uitgebreidere Vertex AI/Gemini GenAI-voorbeelden dan wat hier staat: zie
[GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai)
in de root-README.
