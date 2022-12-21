import boto3
import json
import os

def lambda_handler(event, context):
    try:
        regions = os.getenv('AWS_REGIONS')
        if regions == None:
            regions = get_all_regions()
        elif regions.lower() == 'all':
            regions = get_all_regions()
        else:
            regions = [x.strip() for x in regions.split(',')]
    except:
        regions = []
    results = {}
    for region in regions:
        ec2 = boto3.resource('ec2',region_name=region)
        results[region] = ec2.instances.filter(Filters=[{'Name':'instance-state-name','Values':['running']}]).stop()
    print(json.dumps(results,indent=1))

def get_all_regions():
    client = boto3.client('ec2')
    regions = client.describe_regions()['Regions']
    region_names = [x['RegionName'] for x in regions]
    return region_names