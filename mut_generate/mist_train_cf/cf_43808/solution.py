"""
QUESTION:
Create a serverless application using AWS Lambda and API Gateway by implementing a Python function `lambda_handler(event, context)` that returns a response in the format `{'statusCode': int, 'body': str}`. The function should be able to be deployed on AWS Lambda and integrated with API Gateway.
"""

def lambda_handler(event, context):
    # Run your function code here
    return {
        'statusCode': 200,
        'body': 'Hello, world!'
    }