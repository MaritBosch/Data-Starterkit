-- Self-join template: hiërarchische relatie binnen één tabel (bv. manager-medewerker).

SELECT
    medewerker.<id_kolom>       AS medewerker_id,
    medewerker.<naam_kolom>     AS medewerker_naam,
    manager.<id_kolom>          AS manager_id,
    manager.<naam_kolom>        AS manager_naam
FROM <tabel> AS medewerker
LEFT JOIN <tabel> AS manager
    ON medewerker.<manager_id_kolom> = manager.<id_kolom>
ORDER BY manager_naam, medewerker_naam;

-- Variant: vind medewerkers zonder manager (top van de hiërarchie)
-- WHERE medewerker.<manager_id_kolom> IS NULL

-- Variant: tel het aantal directe rapporten per manager
-- SELECT manager.<naam_kolom>, COUNT(*) AS n_directe_rapporten
-- FROM <tabel> AS medewerker
-- JOIN <tabel> AS manager ON medewerker.<manager_id_kolom> = manager.<id_kolom>
-- GROUP BY 1
-- ORDER BY n_directe_rapporten DESC;
