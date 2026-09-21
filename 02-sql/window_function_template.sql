-- Window function template: waarde deze periode vs. vorige periode, per groep.
--
-- Opbouw (zoals in praktijklog):
--   1. Eerst in gewone taal: "per <groep>, per <periode>, de <metric> van nu naast vorige."
--   2. Basis-aggregatie (CTE 'per_periode').
--   3. Window function erbovenop (LAG).
--   4. Verschil/percentage berekenen in de BUITENSTE laag, niet in dezelfde SELECT.

WITH per_periode AS (
    SELECT
        <groep_kolom>                                  AS groep,
        DATE_TRUNC('month', <datum_kolom>)              AS periode,
        SUM(<metric_kolom>)                             AS metric_waarde
    FROM <tabel>
    GROUP BY 1, 2
),
met_vorige AS (
    SELECT
        groep,
        periode,
        metric_waarde,
        LAG(metric_waarde) OVER (
            PARTITION BY groep
            ORDER BY periode
        )                                                AS metric_vorige_periode
    FROM per_periode
)
SELECT
    groep,
    periode,
    metric_waarde,
    metric_vorige_periode,
    metric_waarde - metric_vorige_periode                                        AS delta_absoluut,
    ROUND(
        100.0 * (metric_waarde - metric_vorige_periode)
        / NULLIF(metric_vorige_periode, 0), 1
    )                                                                             AS delta_pct
FROM met_vorige
ORDER BY groep, periode;

-- Edge case om te testen: een groep met maar 1 periode data — metric_vorige_periode
-- moet dan NULL zijn, en delta_pct moet niet crashen (vandaar NULLIF).
