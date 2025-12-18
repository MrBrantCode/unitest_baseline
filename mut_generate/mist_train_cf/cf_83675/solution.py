"""
QUESTION:
Write a function `lambda_handler` in Python that takes an event and context as input and returns the sum of two numbers passed in the event. The function should be compatible with AWS Lambda.
"""

def lambda_handler(event, context):
    num1 = event['num1']
    num2 = event['num2']
    return {
        "sum": num1 + num2
    }