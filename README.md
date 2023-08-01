# dataengineer-mmv

Este repositorio contiene la solución al ejercicio dividido en dos partes, cada una ubicada en su respectiva carpeta.Cada apartado puede consultarse en el historial de commits.

## Estructura de carpetas

    python/
    ├── main.py
    │
    │
    airflow/
    ├── dags/
    │   ├── test.py
    │
    ├── plugins/
    │   ├── dags_utils.py
    │   └── ...
    └── ...


## Python

La primera parte del ejercicio se encuentra en la carpeta "python" que contiene el siguiente archivo:

    main.py: implementación de las clases requeridas y manipulación de objetos.

## Airflow

La segunda parte del ejercicio se encuentra en la carpeta "airflow".
    
    test.py: contiene el DAG del ejercicio, con cada apartado resuelto en un commit.
    
    dags_utils.py: contiene los operadores y funciones auxiliares creados para resolver el ejercicio.

Para levantar Airflow mediante docker, se ha utilizado el docker-compose.yaml de la documentación oficial (https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).