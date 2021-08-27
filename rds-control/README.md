# RDS Control

Funcion lambda que permite iniciar o detener una instancia RDS de AWS. Esta funcion permite generar control sobre la instancia RDS para optimizar costos y detenerla en ambientes en los cuales no se requiere una disponibilidad 24/7.

## Tabla de Contenido
- [RDS Control](#rds-control)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Lenguaje](#lenguaje)
  - [Evento de entrada](#evento-de-entrada)

## Lenguaje

Esta funcion esta desarrollada en Python, y se puede configurar con (Python 3.6, 3.7 ó 3.8)

```py
import boto3
import os

def lambda_handler(event, context):   

    dbinstance = event['instance_mame']
    operation = event['operation']
    rds = boto3.client('rds')

    if operation == 0:
        rds.stop_db_instance(DBInstanceIdentifier=dbinstance)
        print ("Se detuvo la instancia RDS ", event['instance_mame'])

    elif operation == 1:
        rds.start_db_instance(DBInstanceIdentifier=dbinstance)
        print ("Se inicio la instancia RDS ", event['instance_mame'])
    return {
        'statusCode': 200,
    }
```

## Evento de entrada

El evento de esta funcion recibe el nombre de la instancia RDS y el codigo de la operacion a ejecutar (Iniciar o Detener).

| Operación | Descripcion |
|--|--|
| 1 | Iniciar instancia RDS|
| 0 | Detener instancia RDS|


```json
{
  "instance_mame": "dev-project-oracle-ee-rds",
  "operation": 1
}
```
>En el ejemplo anterior el evento iniciara la instancia RDS con el nombre **dev-project-oracle-ee-rds**.