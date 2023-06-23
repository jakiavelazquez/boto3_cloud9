import boto3

internet_gateway_id = 'igw-06819799e73a8c799'
vpc_id = 'vpc-00710b48a44be3f3a'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)