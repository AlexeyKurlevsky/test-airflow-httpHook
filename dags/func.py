import json
import logging
from typing import Optional

from airflow.models import TaskInstance
from airflow.providers.http.hooks.http import HttpHook


def get_data(ti: TaskInstance, **context) -> Optional[str]:
    hook = HttpHook(method="GET", http_conn_id="my_conn")
    try:
        response = hook.run(endpoint="posts")
        logging.info(f"Status code: {response.status_code}")
        if response.status_code == 200:
            ti.xcom_push(key="data_api", value=json.loads(response.content))
            return "handle_json"
    except Exception as ex:
        logging.error(f"Ошибка вызова: {ex}")


def handle_data(ti: TaskInstance, **context) -> None:
    data = ti.xcom_pull(task_ids="get_data_from_api", key="data_api")
    logging.info(f"Data from api: {data}")
    # TODO: Дальше нужно реализовать необходимую обработку
