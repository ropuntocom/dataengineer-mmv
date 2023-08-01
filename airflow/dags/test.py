from datetime import datetime, timedelta
from airflow import DAG


# argumentos definidos por defecto
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(1900, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
    }

# 1) Define un DAG llamado "test" que se ejecute cada día a las 3:00 UTC con unos argumentos por defecto.
dag = DAG(
    'test',
    default_args=default_args,
    schedule_interval='0 3 * * *',  # expresión crontab todos los días a las 3:00 UTC
    catchup=False  # evita que se ejecuten tareas pasadas al iniciar el DAG
    )
