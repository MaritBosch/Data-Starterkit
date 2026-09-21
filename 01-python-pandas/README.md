# 01 — Python & pandas

Startpunt voor elke data-cleaning/wrangling-klus. Volgt dezelfde 5 stappen als de
"voorbeeldaanpak" in je praktijklog: verkennen → dedupliceren → missende waarden →
features → toelichting.

- `data_cleaning_template.py` — de hoofdflow, als functies die je los kunt aanroepen of
  los kunt testen. Importeer en gebruik in een notebook, of draai als script.
- `data_quality_report.py` — losse, herbruikbare functie die een dataset in één oogopslag
  beoordeelt (nulls, dtypes, duplicaten, outliers). Handig als eerste stap op ELK nieuw
  project, ook buiten cleaning om.

## Gebruik

```bash
python data_cleaning_template.py pad/naar/jouw_databestand.csv
```
