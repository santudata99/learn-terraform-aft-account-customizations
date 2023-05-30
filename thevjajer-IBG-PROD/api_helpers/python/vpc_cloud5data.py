import boto3

def client_init():
  ec2_client = boto3.client("ec2", region_name="us-east-1")
  return ec2_client
  
def vpc_creation(client):
  ec2_client.create_vpc(CidrBlock='172.16.0.0/16')
  
if __name== "__main__":
   ec2_client=client_init()
   vpc_creation(client)
