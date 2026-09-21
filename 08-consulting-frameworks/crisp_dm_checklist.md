# CRISP-DM checklist

Vul per fase in wat voor dit project concreet geldt. Leeg laten mag niet — als je een
regel niet kunt invullen, is dat een signaal dat je die fase nog niet goed hebt gedaan.

## 1. Business understanding
- Welk business-probleem lossen we op (niet: welk data-probleem)?
- Wat is het succescriterium, in business-termen (niet in accuracy/AUC)?
- Wie is de opdrachtgever en wat beslissen zij met de uitkomst?

## 2. Data understanding
- Welke databronnen zijn er, en wie is de eigenaar?
- Eerste kwaliteitsscan: wat valt meteen op (zie ook 01-python-pandas/data_quality_report.py)?

## 3. Data preparation
- Welke cleaning-keuzes zijn gemaakt en waarom (zie 01-python-pandas)?
- Welke features zijn afgeleid en welke vraag beantwoorden ze?

## 4. Modeling
- Welke baseline is gebruikt (zie 03-modelleren)?
- Welk model, en waarom dit model boven alternatieven?

## 5. Evaluation
- Klopt het model met de business-succescriteria uit stap 1 — niet alleen met de
  technische metric?
- Wat zijn de bekende beperkingen?

## 6. Deployment
- Hoe komt dit bij de eindgebruiker terecht (zie 04-cloud-vertex-ai / 05-docker-k8s-cicd)?
- Wie onderhoudt dit na oplevering?

## Wanneer gebruik je CRISP-DM NIET?
(Verplicht invullen — oefen dit tegenargument, zie de voorbeeldaanpak in praktijklog.)
