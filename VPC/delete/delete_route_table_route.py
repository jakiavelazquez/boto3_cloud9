import boto3

route_table_id = 'rtb-08cbe0e725a80f2c9'

ec2 = boto3.client('ec2')

ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)