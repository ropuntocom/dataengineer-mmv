# dags_utils.py

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
