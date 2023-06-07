import boto3

def get_dynamodb_limits():
    dynamodb_client = boto3.client('dynamodb',region_name = 'ap-south-1')
    response = dynamodb_client.describe_limits()

    return response['AccountMaxWriteCapacityUnits']

write_capacity_limit = get_dynamodb_limits()
print(f"Write Capacity Units Limit: {write_capacity_limit}")
