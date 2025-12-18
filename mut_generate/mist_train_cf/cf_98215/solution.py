"""
QUESTION:
Create a `scale_deployment(deployment_name, replicas)` function that scales a deployment based on the provided deployment name and replicas count. Ensure the function checks for valid arguments before execution: `deployment_name` should be a string and `replicas` should be an integer between 1 and 10 (inclusive). If either argument is invalid, return an error message.
"""

def scale_deployment(deployment_name, replicas):
    if not isinstance(deployment_name, str) or not isinstance(replicas, int):
        return "Error: Invalid argument(s)"
    elif replicas < 1 or replicas > 10:
        return "Error: Number of replicas must be between 1 and 10"
    else:
        # actual scaling logic here
        return "Deployment {} scaled to {} replicas".format(deployment_name, replicas)