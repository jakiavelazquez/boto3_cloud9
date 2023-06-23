import boto3

route_table_id = 'rtb-08cbe0e725a80f2c9'
internet_gateway_id = 'igw-06819799e73a8c799'

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)