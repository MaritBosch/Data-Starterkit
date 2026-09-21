"""Deploy een container-image (zie serving_app/) als Vertex AI endpoint.

Test serving_app/ ALTIJD eerst lokaal (uvicorn + curl) vóór je dit script draait.
Vervang de placeholders (PROJECT_ID, REGION, IMAGE_URI) door je eigen waarden.
"""

from __future__ import annotations

from google.cloud import aiplatform

PROJECT_ID = "<jouw-gcp-project-id>"
REGION = "europe-west4"
IMAGE_URI = "europe-west4-docker.pkg.dev/<project>/<repo>/<image>:<tag>"
MODEL_DISPLAY_NAME = "<model-naam>"
ENDPOINT_DISPLAY_NAME = "<endpoint-naam>"


def deploy() -> aiplatform.Endpoint:
    aiplatform.init(project=PROJECT_ID, location=REGION)

    model = aiplatform.Model.upload(
        display_name=MODEL_DISPLAY_NAME,
        serving_container_image_uri=IMAGE_URI,
        serving_container_predict_route="/predict",
        serving_container_health_route="/health",
        serving_container_ports=[8080],
    )

    endpoint = model.deploy(
        deployed_model_display_name=MODEL_DISPLAY_NAME,
        machine_type="n1-standard-2",
        min_replica_count=1,
        max_replica_count=1,
    )

    print(f"Endpoint live: {endpoint.resource_name}")
    print("Vergeet niet: endpoint.undeploy_all() + endpoint.delete() als je klaar bent met testen.")
    return endpoint


if __name__ == "__main__":
    deploy()
