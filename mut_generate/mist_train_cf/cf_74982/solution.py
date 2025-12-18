"""
QUESTION:
Create a function in Python that mimics the AWS Lambda function creation process, taking into account the restrictions and best practices for efficiency and debugging, without any implementation details of AWS Lambda itself.
"""

def create_aws_lambda_function(function_name, runtime, handler, iam_role, memory, timeout):
    """
    Creates an AWS Lambda function.

    Args:
        function_name (str): The name of the Lambda function.
        runtime (str): The runtime environment for the Lambda function (e.g., Node.js).
        handler (str): The entry point of the Lambda function.
        iam_role (str): The IAM role for the Lambda function.
        memory (int): The memory allocation for the Lambda function in MB.
        timeout (int): The timeout for the Lambda function in seconds.

    Returns:
        dict: A dictionary containing the Lambda function configuration.
    """

    # Initialize the Lambda function configuration
    lambda_function = {
        "FunctionName": function_name,
        "Runtime": runtime,
        "Handler": handler,
        "Role": iam_role,
        "MemorySize": memory,
        "Timeout": timeout
    }

    return lambda_function