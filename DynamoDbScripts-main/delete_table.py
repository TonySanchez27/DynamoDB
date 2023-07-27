import boto3

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

try:
    dynamodb.delete_table(TableName='pvcard')
    print("Table deleted successfully.")
except Exception as e:
    print("Could not delete table. Please try again in a moment. Error:")
    print(e)
