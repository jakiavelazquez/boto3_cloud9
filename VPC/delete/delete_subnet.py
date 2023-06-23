import boto3

subnet_id = 'subnet-0e8455b4974955d15'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)