from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="hello_airflow",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["learning", "setup"],
)
def hello_airflow():
    @task
    def start():
        print("Airflow is running correctly.")

    @task
    def process():
        print("This is the first validation DAG for the project.")

    @task
    def finish():
        print("Validation completed successfully.")

    start() >> process() >> finish()


hello_airflow_dag = hello_airflow()
