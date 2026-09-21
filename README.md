# Deep Data Dive — starterkit

Persoonlijke templatebibliotheek: voor elk type opdracht dat in `praktijklog` (je oefentracker)
staat, een werkend startpunt. Niet om te copy-pasten tijdens je closed-book kata's — daar is
het punt juist dat je zonder houvast oefent — maar voor échte projecten: je scriptie, je eerste
weken bij een consultancy, en later Deep Data Dive-opdrachten.

## Regel #1: scheid oefenen en opleveren

- **Kata / closed-book sessie in praktijklog** → geen templates erbij. Dat oefen je juist om
  zonder te kunnen.
- **Een echt project, scriptie-onderdeel, of klantwerk** → begin hier, pas aan, lever op.

Als je deze grens laat vervagen ondermijn je precies het oefenprogramma dat je net hebt
opgezet — dus wees daar zelf streng in.

## Structuur

Elke map komt overeen met één skill uit je praktijklog-tracker, in dezelfde volgorde:

| Map | Skill | Bevat |
|---|---|---|
| `01-python-pandas` | Python & pandas | data cleaning + quality report templates |
| `02-sql` | SQL onder tijdsdruk | window function, CTE, self-join, gaps-and-islands |
| `03-modelleren` | Modelleren & interpreteren | baseline+model+evaluatie, SHAP-interpretatie |
| `04-cloud-vertex-ai` | Cloud deploy | FastAPI serving app, deploy-script, batch predict |
| `05-docker-k8s-cicd` | Docker/K8s/CI-CD | multi-stage Dockerfile, k8s deployment, GitHub Actions |
| `06-dashboards` | Dashboards & visualisatie | één-vraag-één-chart template (Plotly) |
| `07-genai-rag` | GenAI & LLM-integratie | RAG-pipeline + eval-harness |
| `08-consulting-frameworks` | Frameworks paraat | CRISP-DM checklist, ODI Data Ethics Canvas, project charter |
| `09-klant-communicatie` | Vertalen naar business-inzicht | executive summary + STAR-worksheet |

Elke map heeft een eigen `README.md` met wanneer en hoe je 'm gebruikt.

## Dit naar je eigen GitHub zetten

```bash
cd deep-data-dive-starterkit
git init
git add .
git commit -m "Initial starterkit"
```

Maak daarna op github.com een nieuw, leeg (privé) repository aan — géén README/`.gitignore`
aanvinken, dat botst met wat je al hebt — en volg de instructies die GitHub toont onder
"…or push an existing repository from the command line", ongeveer:

```bash
git remote add origin https://github.com/<jouw-gebruikersnaam>/deep-data-dive-starterkit.git
git branch -M main
git push -u origin main
```

Vanaf dan: elke keer dat je een template verbetert na een echt project, commit je dat терug —
zo groeit de kit mee met wat je leert, in plaats van een eenmalige snapshot te blijven.

## Referentie — bredere repo's om naast je eigen kit te leggen

Deze bouwen niets voor je, maar zijn goede naslagwerken als je verder wilt dan wat hier staat:

- [drivendataorg/cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science) — de facto standaard projectstructuur voor data science repo's.
- [GoogleCloudPlatform/vertex-ai-samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples) — officiële Vertex AI-voorbeelden, veel dieper dan de deploy-template hier.
- [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) — Gemini/GenAI-voorbeelden op Google Cloud, relevant voor de RAG-template.
- [GoogleCloudPlatform/vertex-pipelines-end-to-end-samples](https://github.com/GoogleCloudPlatform/vertex-pipelines-end-to-end-samples) — als je later een volledige MLOps-pipeline wilt bouwen, niet alleen een los endpoint.

## requirements.txt

Eén gedeelde requirements-file op root-niveau met de kernlibraries; per map staat er in de
README bij als er iets extra's nodig is (bv. `google-cloud-aiplatform` alleen voor map 04).
