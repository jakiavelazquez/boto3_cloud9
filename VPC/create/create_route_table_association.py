import boto3

route_table_id = 'rtb-08cbe0e725a80f2c9'
subnet_id = 'subnet-0e8455b4974955d15'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id, 
    SubnetId=subnet_id)

print(association['AssociationId'])
