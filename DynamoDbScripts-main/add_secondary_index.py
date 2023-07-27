import boto3

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

try:
    dynamodb.update_table(
        TableName='pvcard',
        AttributeDefinitions=[
            {
                "AttributeName": "phoneNum",
                "AttributeType": "S"
            }
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "PhoneNumIndex",
                    "KeySchema": [
                        {
                            "AttributeName": "phoneNum",
                            "KeyType": "HASH"
                        }
                    ],
                    "Projection": {
                        "ProjectionType": "ALL"
                    },
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 1,
                        "WriteCapacityUnits": 1
                    }
                }
            }
        ],
    )
    print("Table updated successfully.")
except Exception as e:
    print("Could not update table. Error:")
    print(e)
