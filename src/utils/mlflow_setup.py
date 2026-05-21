# model_setup.py

import dagshub
import mlflow

def init_mlflow():
    dagshub.init(
        repo_owner="Japneet-Kaur-Chawla",
        repo_name="youtube-comment-analysis-repository",
        mlflow=True
    )

    mlflow.set_tracking_uri("dagshub")
    mlflow.set_experiment("dvc-pipeline-runs")


