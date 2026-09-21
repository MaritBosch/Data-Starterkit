"""SHAP-interpretatie template.

Doel: top-3 features vertalen naar een zin die een leek snapt, niet een SHAP-plot
zonder uitleg op een klant afvuren.
"""

from __future__ import annotations

import pandas as pd
import shap


def explain_model(model, X_sample: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """Berekent SHAP-waarden en geeft de top_n meest invloedrijke features terug,
    gesorteerd op gemiddelde absolute impact.
    """
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)

    # Bij binaire classificatie geeft TreeExplainer soms een lijst van 2 arrays terug
    values = shap_values[1] if isinstance(shap_values, list) else shap_values

    importance = pd.DataFrame({
        "feature": X_sample.columns,
        "gemiddelde_impact": abs(values).mean(axis=0),
    }).sort_values("gemiddelde_impact", ascending=False)

    top = importance.head(top_n)
    print(f"Top {top_n} features:")
    print(top.to_string(index=False))
    print(
        "\nTODO: vertaal elke regel naar een zin zonder jargon, bv.\n"
        "  '<feature> is de sterkste voorspeller — klanten met een hoge waarde "
        "hier hebben duidelijk meer/minder kans op <uitkomst>.'"
    )
    return top


if __name__ == "__main__":
    print("Importeer explain_model(model, X_sample) na het trainen van je model.")
