# 05 — Docker / K8s / CI-CD

- `Dockerfile.multistage` — multi-stage build die de image-grootte flink verkleint
  t.o.v. een naïeve single-stage Dockerfile (alleen de runtime-dependencies komen in
  de uiteindelijke laag terecht).
- `.dockerignore` — voorkomt dat je `.venv`, `.git`, data-bestanden etc. meebouwt.
- `k8s_deployment_template.yaml` — basis Deployment + Service om een container met
  3 replicas te draaien.
- `.github/workflows/ci_template.yml` — GitHub Actions: eerst tests, dán pas
  build + push van de image. Zo leer je het ook oefenen in je kata: één stap
  tegelijk toevoegen en verifiëren, niet alles ineens.

## Lokaal bouwen en testen

```bash
docker build -f Dockerfile.multistage -t <naam>:test .
docker run -p 8080:8080 <naam>:test
```

## Bewust laten breken (leert je de debug-workflow)

Verander tijdelijk het CMD in de Dockerfile naar iets ongeldigs, build opnieuw, en
lees de foutmelding met `docker logs <container-id>`. Zet 'm daarna terug.
