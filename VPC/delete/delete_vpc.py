import boto3

vpc_id = 'vpc-00710b48a44be3f3a'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)