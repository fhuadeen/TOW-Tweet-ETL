from datetime import timedelta
from textwrap import dedent
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import os

dag = DAG(
    'tweet_etl', default_args=default_args, schedule_interval=timedelta(minutes=10))


t1 = KubernetesPodOperator(
        namespace='airflow',
        image='fhuadeen/tweet_data_producer',
        labels={'dag-id': dag.dag_id},
        name='data-producer',
        task_id='data-producer',
        in_cluster=True,       #False: local, True: cluster               
        cluster_context='minikube',  
        # config_file=os.path.expanduser('~')+"/.kube/config",
        is_delete_operator_pod=True,
        get_logs=True,
        dag=dag
    )