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