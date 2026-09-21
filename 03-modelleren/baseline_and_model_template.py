"""Baseline-vs-model template.

Volgorde (uit praktijklog): baseline eerst -> kies metric bij het probleem -> bouw model
-> vergelijk op DEZELFDE metric -> wees eerlijk over beperkingen.
"""

from __future__ import annotations

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split


def run_baseline_and_model(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_state: int = 42,
) -> dict:
    """Traint een dummy-baseline en een RandomForest, en rapporteert beide op
    dezelfde metrics zodat je een eerlijke vergelijking hebt.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # --- Stap 1: baseline. Als je "echte" model dit niet verslaat, is het niet af. ---
    baseline = DummyClassifier(strategy="most_frequent")
    baseline.fit(X_train, y_train)
    baseline_pred = baseline.predict(X_test)

    # --- Stap 2: kies je metric bij het probleem (hier: scheve klassen -> AUC + F1,
    # niet alleen accuracy) ---
    model = RandomForestClassifier(n_estimators=300, random_state=random_state)
    model.fit(X_train, y_train)
    model_pred = model.predict(X_test)
    model_proba = model.predict_proba(X_test)[:, 1] if len(set(y)) == 2 else None

    print("=== Baseline (dummy) ===")
    print(classification_report(y_test, baseline_pred, zero_division=0))

    print("=== Model (RandomForest) ===")
    print(classification_report(y_test, model_pred, zero_division=0))
    if model_proba is not None:
        print(f"AUC: {roc_auc_score(y_test, model_proba):.3f}")

    return {
        "baseline": baseline,
        "model": model,
        "X_test": X_test,
        "y_test": y_test,
    }


if __name__ == "__main__":
    print(
        "Importeer run_baseline_and_model(X, y) in je eigen script/notebook — "
        "dit bestand draait niet los zonder data."
    )
