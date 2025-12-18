"""
QUESTION:
Configure a Serverless AWS Lambda Function with Node.js Runtime to Resolve 'Internal Server Error'

Configure a serverless function using AWS Lambda with the Node.js runtime to bypass 'Internal Server Error'. Create a function named `lambda_handler` that takes an event and context as parameters, and returns a response. Ensure the function has the necessary permissions to execute and access AWS services, and that the Node.js version compatibility is taken into account.
"""

def lambda_handler(event, context):
    try:
        # Add your function code here to handle the event
        # For example:
        response = {
            'statusCode': 200,
            'body': 'Hello from Lambda!'
        }
        return response
    except Exception as e:
        # Handle any exceptions here
        print(f"An error occurred: {str(e)}")
        response = {
            'statusCode': 500,
            'body': 'Internal Server Error'
        }
        return response