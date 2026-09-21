"""Eén-vraag-één-chart template.

Regel: je kunt deze functie niet aanroepen zonder een `conclusie` op te geven — dat
dwingt je om eerst de titel/conclusie te bepalen, en pas daarna de chart te bouwen.
Dat is de kern van de voorbeeldaanpak uit praktijklog.
"""

from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go


def one_question_chart(
    df: pd.DataFrame,
    x: str,
    y: str,
    conclusie: str,
    group: str | None = None,
) -> go.Figure:
    """Bouwt één lijn/bar-chart die precies één vraag beantwoordt.

    Args:
        df: data.
        x, y: kolomnamen voor de assen.
        conclusie: VERPLICHT — de titel wordt de conclusie, niet de metric-naam.
            Bijv. "Omzet daalt sinds juni bij klantsegment B", niet "Omzet per maand".
        group: optionele kolom om meerdere lijnen te tekenen.
    """
    if not conclusie:
        raise ValueError(
            "Geen conclusie meegegeven. Bepaal eerst welke conclusie deze chart moet "
            "overtuigen, vóór je 'm bouwt."
        )

    fig = go.Figure()
    if group:
        for key, sub in df.groupby(group):
            fig.add_trace(go.Scatter(x=sub[x], y=sub[y], mode="lines+markers", name=str(key)))
    else:
        fig.add_trace(go.Scatter(x=df[x], y=df[y], mode="lines+markers"))

    fig.update_layout(
        title=conclusie,
        xaxis_title=x,
        yaxis_title=y,
        template="plotly_white",
    )
    return fig


if __name__ == "__main__":
    print(
        "Importeer one_question_chart(df, x, y, conclusie) — 'conclusie' is verplicht, "
        "met opzet."
    )
