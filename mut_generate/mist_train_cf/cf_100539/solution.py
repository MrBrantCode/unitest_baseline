"""
QUESTION:
Write a function `scale_deployment(deployment_name, replicas)` that scales a deployment to the specified number of replicas. The function should return an error message if `deployment_name` is not a string or `replicas` is not an integer. Additionally, the function should return an error message if `replicas` is less than 1 or greater than 10. If both arguments are valid, the function should return a success message.
"""

def scale_deployment(deployment_name, replicas):
    if not isinstance(deployment_name, str) or not isinstance(replicas, int):
        return "Error: Invalid argument(s)"
    elif replicas < 1 or replicas > 10:
        return "Error: Number of replicas must be between 1 and 10"
    else:
        return "Deployment {} scaled to {} replicas".format(deployment_name, replicas)