from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.models.baseoperator import cross_downstream

from plugins.dags_utils import split_tasks
from plugins.dags_utils import TimeDiff

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

    # 3) Define una lista de tareas dummy task_n con N tareas, donde cada tarea con n par dependa de todas las tareas impares.
    N=5
    tasks = [DummyOperator(task_id=f'task_{i}') for i in range(1, N+1)] # lista con N tareas dummy
    pares, impares = split_tasks(tasks)

    # 4) Define un nuevo operador TimeDiff que parta del BaseOperator, que reciba una fecha (diff_date) como entrada y muestre la diferencia con la actual. Crea una tarea nueva con el operador.
    diff_date_task = TimeDiff(
            task_id = 'task_diff_date',
            diff_date = datetime(2023, 7, 31),  # Fecha de ejemplo para la diferencia de tiempo.
            )

    # dependencias
    start >> impares
    cross_downstream(impares, pares) 
    pares >> diff_date_task >> end