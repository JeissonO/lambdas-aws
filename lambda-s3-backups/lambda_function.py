import logging
import boto3
import datetime
from botocore.exceptions import ClientError
from datetime import date

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s: %(message)s')
                        
    bucket_name = 'bucketname'
    env = 'sandboc'
    ext = '.backup'
    
    # Concat the object name to find an specific file. 
    today = date.today()
    day_backup = today.strftime("%Y_%m_%d")+env+ext    
    print("day_backup =", day_backup)
    
    copyBackupFile(bucketname,objectname):
    readmetadata(bucket_name ,day_backup)
    updateMetadata(bucket_name ,day_backup)
    validateMetadata(bucket_name ,day_backup)
    
    if validateMetadata(bucket_name ,day_backup):
        print("salvado")
    
    objects = list_bucket_objects(bucket_name)
    
    if objects is not None:
        # List the object names
        logging.info(f'Objects in {bucket_name}')
        count = len(objects)
        print(f'Backup count: {count}')
        for obj in objects:            
            print(f'object : {obj["Key"]}')

    return True

def list_bucket_objects(bucket_name):
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return None
    return response['Contents']

def readmetadata (bucketname,objectname):
    try:
        object = s3.get_object(Bucket=bucketname, Key=objectname)
        object_metadata=object['Metadata']
        print (f'Metadata = {object_metadata}')
    except ClientError as e:
        logging.error(e)
        
def updateMetadata(bucketname,objectname):
    s3_object = s3.get_object(Bucket=bucketname, Key=objectname)
    k = s3.head_object(Bucket = bucketname, Key = objectname)
    m = k["Metadata"]
    m["store_glacer"]= "true"
    s3.copy_object(Bucket = bucketname, Key = objectname, CopySource = bucketname + '/' + objectname, Metadata = m, MetadataDirective='REPLACE')
    return None
    
def validateMetadata(bucketname,objectname):
    s3_object = s3.get_object(Bucket=bucketname, Key=objectname)
    k = s3.head_object(Bucket = bucketname, Key = objectname)
    m = k["Metadata"]
    try:
        value = m["store_glacer"]
        if value:
            return True
        else:
            return False
    except KeyError as e:
        return False
        
def copyBackupFile(bucketname,objectname):
    newKey = "glacer_"+objectname
    copy_source = {'Bucket': bucketname, 'Key': objectname }
    s3.copy_object(CopySource = copy_source, Bucket = bucketname , Key = newKey, StorageClass= 'GLACIER')    
    return None