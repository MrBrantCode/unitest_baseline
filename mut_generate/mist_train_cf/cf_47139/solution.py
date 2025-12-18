"""
QUESTION:
Configure a serverless function via AWS Lambda for Node.js runtime with the function name `deploy_lambda_nodejs`. Implement error management and debugging strategies, and incorporate security considerations to prevent potential risks. The function should be deployable using the Serverless Framework and follow best practices for IAM user creation, logging, and monitoring.
"""

def deploy_lambda_nodejs(event, context):
    try:
        # function code here
        return {
            'statusCode': 200,
            'body': 'Function executed successfully'
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': 'Error occurred while executing function'
        }