"""Batch-predictiejob template — voor als je geen realtime endpoint nodig hebt.

Gebruik dit wanneer voorspellingen periodiek (bv. dagelijks) mogen draaien in plaats
van on-demand — vaak goedkoper en simpeler dan een levend endpoint onderhouden.
"""

from __future__ import annotations

from google.cloud import aiplatform

PROJECT_ID = "<jouw-gcp-project-id>"
REGION = "europe-west4"
MODEL_RESOURCE_NAME = "<projects/.../models/...>"
INPUT_URI = "gs://<bucket>/input/*.jsonl"
OUTPUT_URI_PREFIX = "gs://<bucket>/output/"


def run_batch_prediction() -> aiplatform.BatchPredictionJob:
    aiplatform.init(project=PROJECT_ID, location=REGION)

    model = aiplatform.Model(MODEL_RESOURCE_NAME)

    job = model.batch_predict(
        job_display_name="batch-predict-job",
        gcs_source=INPUT_URI,
        gcs_destination_prefix=OUTPUT_URI_PREFIX,
        machine_type="n1-standard-4",
        sync=True,  # False als je niet wilt wachten tot de job klaar is
    )

    print(f"Batch job status: {job.state}")
    print(f"Output: {OUTPUT_URI_PREFIX}")
    return job


if __name__ == "__main__":
    run_batch_prediction()
