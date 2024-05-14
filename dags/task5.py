import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from func import get_data, handle_data


default_args = {
    "retries": 2,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    catchup=False,
    dag_id="Get_data",
    start_date=datetime.datetime(2024, 1, 27),
    schedule="@daily",
    max_active_runs=1,
    default_args=default_args,
) as dag:
    get_data_from_api = BranchPythonOperator(
        task_id="get_data_from_api",
        python_callable=get_data,
        provide_context=True,
    )

    handle_json = PythonOperator(
        task_id="handle_json",
        python_callable=handle_data,
        provide_context=True,
    )

    get_data_from_api >> handle_json
