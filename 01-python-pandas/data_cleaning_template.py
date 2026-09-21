"""Data-cleaning template — volgt de 5-stappen-aanpak uit praktijklog:

1. Verken blind (zie data_quality_report.py) voordat je iets aanpast.
2. Dedupliceer — bepaal EERST wat een duplicaat betekent voor dit domein.
3. Missende waarden — per kolom bewust kiezen, niet automatisch met mean/median.
4. Afgeleide features — elke feature beantwoordt een concrete vraag.
5. Sluit af met een korte log van je keuzes.

Vervang de placeholder-logica in elke functie door wat past bij jouw dataset —
dit is een skelet, geen kant-en-klare oplossing.
"""

from __future__ import annotations

import sys

import pandas as pd

from data_quality_report import quality_report


def load(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def deduplicate(df: pd.DataFrame, subset: list[str] | None = None) -> pd.DataFrame:
    """Bepaal EERST: is een duplicaat een exacte rij-match, of een match op een subset
    kolommen (bv. klant_id + datum)? Pas dan pas drop_duplicates() toepassen."""
    before = len(df)
    cleaned = df.drop_duplicates(subset=subset, keep="last")
    print(f"Dedupliceren: {before - len(cleaned)} rijen verwijderd (subset={subset}).")
    return cleaned


def handle_missing(df: pd.DataFrame, strategy: dict[str, str]) -> pd.DataFrame:
    """strategy: {'kolomnaam': 'median' | 'mode' | 'zero' | 'flag' | 'drop'}

    Bewust per kolom, geen blanket .fillna(0) of .fillna(mean()) over de hele dataset.
    'flag' betekent: missing is zelf betekenisvol -> vervang door een aparte categorie.
    """
    out = df.copy()
    for col, how in strategy.items():
        if how == "median":
            out[col] = out[col].fillna(out[col].median())
        elif how == "mode":
            out[col] = out[col].fillna(out[col].mode(dropna=True).iloc[0])
        elif how == "zero":
            out[col] = out[col].fillna(0)
        elif how == "flag":
            out[col] = out[col].fillna("__missing__")
        elif how == "drop":
            out = out.dropna(subset=[col])
        else:
            raise ValueError(f"Onbekende strategie '{how}' voor kolom '{col}'")
    return out


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Voeg hier features toe die een concrete vraag beantwoorden.

    Voorbeeld-patroon (pas aan naar jouw kolommen):
        out["dagen_sinds_laatste_actie"] = (pd.Timestamp.now() - out["laatste_actie"]).dt.days
        out["is_weekend"] = out["datum"].dt.dayofweek >= 5
    """
    out = df.copy()
    # TODO: vervang door je eigen features
    return out


def summarize_choices(notes: list[str]) -> None:
    """3-4 zinnen over je keuzes — dit is wat een collega/klant nodig heeft."""
    print("\n--- Samenvatting van cleaning-keuzes ---")
    for n in notes:
        print(f"- {n}")


def run(path: str) -> pd.DataFrame:
    df = load(path)
    print(quality_report(df).to_string(index=False))

    df = deduplicate(df, subset=None)  # TODO: vul subset in als relevant
    df = handle_missing(df, strategy={})  # TODO: vul per kolom in
    df = engineer_features(df)

    summarize_choices([
        "TODO: welke dedupe-regel heb je gekozen en waarom",
        "TODO: welke kolommen kregen welke missing-strategie",
        "TODO: welke features heb je toegevoegd en welke vraag beantwoorden ze",
    ])
    return df


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gebruik: python data_cleaning_template.py pad/naar/bestand.csv")
        raise SystemExit(1)
    result = run(sys.argv[1])
    print(f"\nKlaar. Resultaat: {result.shape[0]} rijen x {result.shape[1]} kolommen.")
