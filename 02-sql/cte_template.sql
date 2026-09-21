-- Geneste CTE template: filter -> aggregeer -> join, in leesbare stappen.
-- Elke CTE doet precies één ding — dat maakt 'm makkelijker te debuggen dan één
-- grote geneste subquery.

WITH gefilterd AS (
    -- Stap 1: filter ruwe rijen vóór je iets aggregeert (sneller + duidelijker)
    SELECT *
    FROM <brontabel>
    WHERE <datum_kolom> >= '<startdatum>'
      AND <status_kolom> = '<gewenste_status>'
),
geaggregeerd AS (
    -- Stap 2: aggregeer per de sleutel die je nodig hebt
    SELECT
        <groep_kolom>          AS groep,
        COUNT(*)                AS n_rijen,
        SUM(<metric_kolom>)     AS totaal_metric
    FROM gefilterd
    GROUP BY 1
),
verrijkt AS (
    -- Stap 3: join pas nadat je hebt gefilterd en geaggregeerd — kleinere joins,
    -- minder kans op onbedoelde duplicatie van rijen door de join
    SELECT
        g.groep,
        g.n_rijen,
        g.totaal_metric,
        d.<attribuut_kolom>     AS extra_context
    FROM geaggregeerd g
    LEFT JOIN <dimensietabel> d
        ON g.groep = d.<sleutel_kolom>
)
SELECT *
FROM verrijkt
ORDER BY totaal_metric DESC;
