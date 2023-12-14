from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.kubernetes.volume import Volume
from airflow.kubernetes.volume_mount import VolumeMount
import datetime
import os
from airflow import DAG
from airflow.utils.dates import days_ago


args = {
    "project_id": "train_and_compare_models-1214192548",
}


dag = DAG(
    "train_and_compare_models-1214192548",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.12.0 pipeline editor using `train_and_compare_models.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: telecom-customer-churn-airflow/include/notebooks/process_data.ipynb

op_9ca028c1_8616_4fee_971f_f8225b23a7c9 = KubernetesPodOperator(
    name="process_data",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com --cos-bucket airflow-bucket --cos-directory 'train_and_compare_models-1214192548' --cos-dependencies-archive 'process_data-9ca028c1-8616-4fee-971f-f8225b23a7c9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/process_data.ipynb' "
    ],
    task_id="process_data",
    env_vars={
        "AWS_S3_ENDPOINT": "https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com",
        "AWS_S3_BUCKET": "airflow-bucket",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "mlpminio",
        "AWS_SECRET_ACCESS_KEY": "#MLPminio4927%",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_9ca028c1_8616_4fee_971f_f8225b23a7c9.image_pull_policy = "Always"


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb

op_819bd5cd_a021_4ce6_80b4_fc119da9fb73 = KubernetesPodOperator(
    name="model_randomforest",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com --cos-bucket airflow-bucket --cos-directory 'train_and_compare_models-1214192548' --cos-dependencies-archive 'model_randomforest-819bd5cd-a021-4ce6-80b4-fc119da9fb73.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_randomforest.ipynb' "
    ],
    task_id="model_randomforest",
    env_vars={
        "AWS_S3_ENDPOINT": "https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com",
        "AWS_S3_BUCKET": "airflow-bucket",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "mlpminio",
        "AWS_SECRET_ACCESS_KEY": "#MLPminio4927%",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_819bd5cd_a021_4ce6_80b4_fc119da9fb73.image_pull_policy = "Always"

op_819bd5cd_a021_4ce6_80b4_fc119da9fb73 << op_9ca028c1_8616_4fee_971f_f8225b23a7c9


# Operator source: telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb

op_6ce8942a_82e1_4599_a195_30ba5459e2a7 = KubernetesPodOperator(
    name="model_gradient_boost",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com --cos-bucket airflow-bucket --cos-directory 'train_and_compare_models-1214192548' --cos-dependencies-archive 'model_gradient_boost-6ce8942a-82e1-4599-a195-30ba5459e2a7.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/model_gradient_boost.ipynb' "
    ],
    task_id="model_gradient_boost",
    env_vars={
        "AWS_S3_ENDPOINT": "https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com",
        "AWS_S3_BUCKET": "airflow-bucket",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "mlpminio",
        "AWS_SECRET_ACCESS_KEY": "#MLPminio4927%",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_6ce8942a_82e1_4599_a195_30ba5459e2a7.image_pull_policy = "Always"

op_6ce8942a_82e1_4599_a195_30ba5459e2a7 << op_9ca028c1_8616_4fee_971f_f8225b23a7c9


# Operator source: telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 = KubernetesPodOperator(
    name="compare_and_push",
    trigger_rule="all_success",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L file:///opt/app-root/lib/python3.8/site-packages/elyra/kfp/bootstrapper.py --output bootstrapper.py && echo 'Downloading file:///elyra-deps/requirements-elyra.txt' && echo 'Downloading file:///elyra-deps/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L file:///elyra-deps/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'train_and_compare_models' --cos-endpoint https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com --cos-bucket airflow-bucket --cos-directory 'train_and_compare_models-1214192548' --cos-dependencies-archive 'compare_and_push-5c7a887a-6833-4b0e-8795-e0b8bbd6d2b9.tar.gz' --file 'telecom-customer-churn-airflow/include/notebooks/compare_and_push.ipynb' "
    ],
    task_id="compare_and_push",
    env_vars={
        "AWS_S3_ENDPOINT": "https://minio-api-mlp-minio.apps.cluster-7ls97.7ls97.sandbox1754.opentlc.com",
        "AWS_S3_BUCKET": "airflow-bucket",
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "mlpminio",
        "AWS_SECRET_ACCESS_KEY": "#MLPminio4927%",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "train_and_compare_models-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9.image_pull_policy = "Always"

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 << op_819bd5cd_a021_4ce6_80b4_fc119da9fb73

op_5c7a887a_6833_4b0e_8795_e0b8bbd6d2b9 << op_6ce8942a_82e1_4599_a195_30ba5459e2a7
