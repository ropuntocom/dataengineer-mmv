from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator


# argumentos definidos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
    }

# 1) Define un DAG llamado "test" que se ejecute cada día a las 3:00 UTC con unos argumentos por defecto.
with DAG(
    'test',
    default_args=default_args,
    schedule_interval='0 3 * * *',  # expresión crontab todos los días a las 3:00 UTC
    catchup=False  # evita que se ejecuten tareas pasadas al iniciar el DAG
    ) as dag:

    # 2) Incluye las tareas start y end como DummyOperator y que end vaya detrás de start en el DAG.
    # tarea start
    start = DummyOperator(
            task_id = 'start')
    # tarea end
    end = DummyOperator(
            task_id = 'end')
    # dependencias
    start >> end
