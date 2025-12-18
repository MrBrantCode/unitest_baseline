"""
QUESTION:
Write a Python function named `lambda_handler` that represents an AWS Lambda function that accepts an event and context as input parameters, and returns a dictionary with a "statusCode" of 200. The function should be idempotent and not cause side effects when invoked multiple times with the same input parameters. Implement the function without using any external libraries or frameworks and assuming that the input event is a dictionary.
"""

def lambda_handler(event, context):
    return {
        "statusCode": 200
    }