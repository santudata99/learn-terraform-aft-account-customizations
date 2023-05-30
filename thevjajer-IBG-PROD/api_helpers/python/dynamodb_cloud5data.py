import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

table = dynamodb.create_table(
    TableName='aftdynamo_cloud5data',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  #Partition_key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  #Sort_key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
