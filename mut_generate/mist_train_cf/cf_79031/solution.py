"""
QUESTION:
Write a function named `my_handler` that handles potential errors in an AWS Lambda function. The function should take two parameters: `event` and `context`, and return a dictionary with a `statusCode` and a `body` containing a JSON-formatted message. The function should log errors to CloudWatch Logs and handle exceptions. The return dictionary should have a `statusCode` of 200 for success and 500 for error.
"""

import json
import logging

def my_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    try:
        # Your code here
        pass
    except Exception as e:
        logger.error('Error: ' + str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }