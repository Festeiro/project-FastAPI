import boto3
from botocore.exceptions import NoCredentialsError

class DynamoDBConnection:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name

    def connect(self):
        try:
            if self.aws_access_key_id and self.aws_secret_access_key and self.region_name:
                dynamodb = boto3.resource(
                    'dynamodb',
                    aws_access_key_id=self.aws_access_key_id,
                    aws_secret_access_key=self.aws_secret_access_key,
                    region_name=self.region_name
                )
            else:
                dynamodb = boto3.resource('dynamodb')
            return dynamodb
        except NoCredentialsError as e:
            print("Error: Unable to connect to DynamoDB. Check your AWS credentials.")
            raise e
