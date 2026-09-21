# 04 — Cloud deploy (Vertex AI)

Volgorde uit je praktijklog-voorbeeldaanpak: begin met het kleinst mogelijke werkende
ding, test lokaal vóór je naar de cloud pusht, deploy, check logging mee, en ruim op.

- `serving_app/` — een minimale FastAPI-app die een gepickled model laadt en op
  `/predict` voorspellingen teruggeeft. Test dit ALTIJD eerst lokaal met
  `uvicorn main:app --reload` en een losse curl-call, vóór je 'm naar Vertex AI pusht.
- `deploy_endpoint_template.py` — script dat een container-image als Vertex AI endpoint
  deployt via de `google-cloud-aiplatform` SDK.
- `batch_predict_template.py` — voor als je geen realtime endpoint nodig hebt, maar
  periodiek een batch aan voorspellingen wilt genereren.

## Lokaal testen (eerst dit, altijd)

```bash
cd serving_app
pip install -r requirements.txt
uvicorn main:app --reload
curl -X POST localhost:8000/predict -H "Content-Type: application/json" \
     -d '{"features": [0.1, 0.2, 0.3]}'
```

## Opruimen

Vergeet niet je endpoint te undeployen na een test — een levend Vertex AI-endpoint
blijft doorlopend kosten maken:

```python
endpoint.undeploy_all()
endpoint.delete()
```
