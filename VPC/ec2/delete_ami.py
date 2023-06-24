import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-0ce50d8de144792b6'
)