"""Snelle, herbruikbare data-quality check.

Draai dit als eerste stap op ELKE nieuwe dataset, vóór je iets anders doet.
Meet eerst hoe vuil de data is — pas dan cleanen.
"""

from __future__ import annotations

import pandas as pd


def quality_report(df: pd.DataFrame, id_cols: list[str] | None = None) -> pd.DataFrame:
    """Geeft per kolom: dtype, % missing, # unieke waarden, en of er outliers zijn (IQR-methode).

    Args:
        df: de dataset om te beoordelen.
        id_cols: kolommen die je NIET als numeriek/outlier wilt behandelen (bv. klant_id).

    Returns:
        Een samenvattend DataFrame, één rij per kolom — dit is wat je in 30 seconden
        moet kunnen doorlezen om te weten of een dataset "clean genoeg" is.
    """
    id_cols = id_cols or []
    rows = []
    for col in df.columns:
        s = df[col]
        row = {
            "kolom": col,
            "dtype": str(s.dtype),
            "pct_missing": round(s.isna().mean() * 100, 1),
            "n_unique": s.nunique(dropna=True),
        }
        if pd.api.types.is_numeric_dtype(s) and col not in id_cols:
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            row["n_outliers_iqr"] = int(((s < lower) | (s > upper)).sum())
        else:
            row["n_outliers_iqr"] = None
        rows.append(row)

    report = pd.DataFrame(rows).sort_values("pct_missing", ascending=False)
    n_dupes = df.duplicated().sum()
    print(f"Rijen: {len(df):,} · Kolommen: {df.shape[1]} · Exacte duplicaten: {n_dupes}")
    return report


if __name__ == "__main__":
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else None
    if not path:
        print("Gebruik: python data_quality_report.py pad/naar/bestand.csv")
        raise SystemExit(1)

    data = pd.read_csv(path)
    print(quality_report(data).to_string(index=False))
