#!/bin/bash

echo "Executing Pre-API Helpers"
#echo "santu VPC_EC2 DynamoDB testing for DevOps team"
#python ./$CUSTOMIZATION/api_helpers/python/vpc_ec2_cloud5data.py &

echo "santu DynamoDB testing for DevSecOps team"
python ./$CUSTOMIZATION/api_helpers/python/dynamo_cloud5data.py
