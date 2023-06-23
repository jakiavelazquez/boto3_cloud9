import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-0bf226490c75c4c36',
    Name='My go to Ami',
)

print(response['ImageId'])