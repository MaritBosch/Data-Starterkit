-- Gaps-and-islands template: vind opeenvolgende periodes zonder onderbreking.
-- Klassieke SQL-vraag bij data-consultancies (bv. "aaneengesloten actieve maanden per klant").
--
-- Truc: nummer de rijen per klant op volgorde (rn), trek dat af van de periode-index.
-- Rijen die bij elkaar horen (geen gap) krijgen dezelfde "eiland"-waarde.

WITH genummerd AS (
    SELECT
        <klant_kolom>                                          AS klant,
        <periode_kolom>                                        AS periode,
        ROW_NUMBER() OVER (
            PARTITION BY <klant_kolom>
            ORDER BY <periode_kolom>
        )                                                       AS rn
    FROM <tabel_met_één_rij_per_actieve_periode>
),
eilanden AS (
    SELECT
        klant,
        periode,
        -- periode (als maandnummer) min rn is constant binnen een aaneengesloten reeks
        (EXTRACT(YEAR FROM periode) * 12 + EXTRACT(MONTH FROM periode)) - rn   AS eiland_id
    FROM genummerd
)
SELECT
    klant,
    eiland_id,
    MIN(periode)  AS reeks_start,
    MAX(periode)  AS reeks_eind,
    COUNT(*)      AS n_periodes_aaneengesloten
FROM eilanden
GROUP BY klant, eiland_id
ORDER BY klant, reeks_start;
