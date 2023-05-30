import boto3
 
def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0715c1897453cabd1",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="cloud5data_ec2"
    )
 
    print('The instance launched in ${region_name}' ["Instances"][0]["InstanceId"])
 
create_instance()
