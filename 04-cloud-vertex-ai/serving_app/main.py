"""Minimale FastAPI serving-app voor een sklearn-achtig model.

Start het kleinst mogelijke werkende ding eerst: laat dit endpoint draaien met een
dummy-model dat altijd hetzelfde teruggeeft, en vervang dan pas model.pkl door je
echte, getrainde model.
"""

from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="model-serving-template")

MODEL_PATH = Path(__file__).parent / "model.pkl"
_model = None


def get_model():
    global _model
    if _model is None:
        if MODEL_PATH.exists():
            with open(MODEL_PATH, "rb") as f:
                _model = pickle.load(f)
        else:
            # Fallback zodat het endpoint sowieso draait, ook zonder model.pkl —
            # vervang dit door een echte foutmelding zodra je een model hebt.
            class _Dummy:
                def predict(self, X):
                    return np.zeros(len(X))

            _model = _Dummy()
    return _model


class PredictRequest(BaseModel):
    features: list[float]


class PredictResponse(BaseModel):
    prediction: float


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    model = get_model()
    X = np.array(req.features).reshape(1, -1)
    pred = model.predict(X)[0]
    return PredictResponse(prediction=float(pred))
