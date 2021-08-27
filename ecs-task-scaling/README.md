# ECS Task Scaling

Función lambda que permite escalar todas las task de un cluster de ECS al numero especificado en los parámetros de entrada. Esto facilita la configuración de eventos o tareas para manejar la disponibilidad de las tareas de acuerdo a las necesidades del proyecto.

## Tabla de Contenido
- [ECS Task Scaling](#ecs-task-scaling)
  - [Tabla de Contenido](#tabla-de-contenido)
  - [Lenguaje](#lenguaje)
  - [Evento de entrada](#evento-de-entrada)

## Lenguaje

Esta función esta desarrollada en Python, y se puede configurar con (Python 3.6, 3.7 ó 3.8)

```py
import boto3
import os
def lambda_handler(event, context):   
    ecs_cluster = event["cluster"]
    ecs = boto3.client('ecs')
    list_services = ecs.list_services(cluster=ecs_cluster)
    listArn = list_services['serviceArns']
    print ("Numero de Instancias: ", event["count"])
    i = 0
    while i < len(listArn) :
        response = ecs.update_service(
            cluster = ecs_cluster,
            service = listArn[i],
            desiredCount = event["count"]
        )
        i += 1
    return {
        'statusCode': 200
    }
```

## Evento de entrada

El evento de esta funcion recibe el nombre del cluster de ECS en el cual se desean escalar las tareas y el valor del numero de instancias de las tareas.

```json
{ 
	"cluster": "test-ecs-cluster", 
	"count": 1 
}
```
>En el ejemplo anterior el evento escalara todas las tareas del cluster **test-ecs-cluster** a 1. 