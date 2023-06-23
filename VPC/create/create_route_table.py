import boto3

vpc_id = 'vpc-00710b48a44be3f3a'

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId=vpc_id)

print(routeTable['RouteTable']['RouteTableId'])