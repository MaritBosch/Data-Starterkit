# 02 — SQL

Vier terugkerende patronen die in vrijwel elk consultancyproject en elk SQL-interview
langskomen. Elke file heeft placeholders (`<tabel>`, `<kolom>`) en een korte uitleg van
de opbouwstappen uit je praktijklog-voorbeeldaanpak: eerst in gewone taal, dan de basis-
aggregatie, dan pas de window function/CTE erbovenop.

| File | Patroon | Wanneer gebruik je dit |
|---|---|---|
| `window_function_template.sql` | LAG/LEAD/RANK | vergelijking t.o.v. vorige periode, ranking binnen groepen |
| `cte_template.sql` | geneste CTE's | multi-stap filter → aggregatie → join, leesbaar houden |
| `self_join_template.sql` | self-join | hiërarchische relaties (bv. manager-medewerker) |
| `gaps_and_islands_template.sql` | gaps & islands | opeenvolgende periodes zonder onderbreking vinden |

Dialect: geschreven in ANSI SQL / PostgreSQL-stijl. Voor BigQuery vervang je
`DATE_TRUNC('month', kolom)` door `DATE_TRUNC(kolom, MONTH)`, en window-function-syntax
blijft nagenoeg gelijk.
