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