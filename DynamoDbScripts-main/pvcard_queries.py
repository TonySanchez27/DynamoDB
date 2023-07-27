import boto3
import sys
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
table = dynamodb.Table('pvcard')

if len(sys.argv) > 1:
    query = sys.argv[1]
    match query:
        case '-c':
            #query for metadata of a person by their cid
            response = table.query(KeyConditionExpression = Key("PK").eq("CID#" + sys.argv[2]) & Key("SK").eq("METADATA#" + sys.argv[2]))
        case '-p':
            #query for metadata of a person by their phone num 
            response = table.query(IndexName= "PhoneNumIndex", KeyConditionExpression = Key("phoneNum").eq(sys.argv[2]))
        case '-v':
            #query for verifier metadata
            response = table.query(KeyConditionExpression = Key("PK").eq("VID#" + sys.argv[2]) & Key("SK").eq("METADATA#" + sys.argv[2]))
        case '-r': #query for requests
            if len(sys.argv) > 2: #filter on sort key with entered date
                response = table.query(KeyConditionExpression = Key("PK").eq("CID#" + sys.argv[2]) & Key("SK").begins_with("TIME#" + sys.argv[3]))
            else: #grab all requests from cid
                response = table.query(KeyConditionExpression = Key("PK").eq("CID#" + sys.argv[2]))
        case '-a':
            #query for pvcma alert
            response = table.query(KeyConditionExpression = Key("PK").eq("DATE#" + sys.argv[2]))
        case '-h':
            # LIST OF COMMANDS
            response = { "Items" : " Query commands: \n -c: CID \n -v: VID \n -r: request \n -a: alert \n to run enter command argument followed by the PK and or SK for the query \n example: python3 pvcard_queries.py -c 123514 " }
    if response:    
        print(json.dumps(response['Items'], indent=4))
    else: 
        print("could not find the entered value in the database. Please try again")
else:
    print("please enter a command or -h for list of commands \n --> python3 pvcard_queries.py -h")


            