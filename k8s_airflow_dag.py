from datetime import timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    'scraping',
    default_args=default_args,
    description='A scraping DAG',
    schedule_interval=timedelta(days=1),
)

k = KubernetesPodOperator(
    namespace='default',
    name="try-scraping",
    image="gcr.io/abiding-state-349605/scrap",
    task_id="try-scraping",
    dag=dag
)

