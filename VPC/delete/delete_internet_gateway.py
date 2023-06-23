import boto3

internet_gateway_id = 'igw-06819799e73a8c799'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)