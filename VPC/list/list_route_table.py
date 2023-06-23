import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_route_tables()

for routeTable in response['RouteTables']:
    print(routeTable['VpcId'], routeTable['RouteTableId'])
    
    for association in routeTable['Associations']:
        print(association['RouteTableAssociationId'])
        if 'Subnet Id' in association:
            print(association['Subnet Id'])
            
    for route in routeTable['Routes']:
        print(route['DestinationCidrBlock'], route['GatewayId'])
