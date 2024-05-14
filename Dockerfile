FROM apache/airflow:2.8.1-python3.10

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY ./dags /opt/airflow/dags/
# COPY ./src /opt/airflow/dags/src/
# COPY ./config /opt/airflow/dags/config