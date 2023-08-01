# dags_utils.py
from airflow.models.baseoperator import BaseOperator
from datetime import datetime

def split_tasks(tasks: list) -> (list,list):
    """
    Data una lista, devuelve dos listas con los elementos pares e impares respectivamente.

    args: 
        task(list): lista con los N elementos a separar

    return:
        pares(list): lista con los elementos pares de la lista original
        impares(list): lista con los elementos impares de la lista original

    """
    pares = []
    impares = []

    for i in range(1, len(tasks)+1):
        if i % 2 == 0: 
            pares.append(tasks[i-1])
        else:
            impares.append(tasks[i-1])

    return pares, impares


# 4) Define un nuevo operador TimeDiff que parta del BaseOperator, que reciba una fecha (diff_date) como entrada y muestre la diferencia con la actual. Crea una tarea nueva con el operador.
class TimeDiff(BaseOperator):
    def __init__(self, diff_date: datetime, **kwargs) -> None:
        super().__init__(**kwargs)
        self.diff_date = diff_date

    def execute(self, context):
        current_date = datetime.utcnow()
        time_difference = current_date - self.diff_date
        self.log.info(f'Time difference: {time_difference}') # la diferencia entre la fecha de entrada y la actual aparecerá en el log