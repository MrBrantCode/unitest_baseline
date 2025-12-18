"""
QUESTION:
Create a function named `process` in a class named `SGDefaultVpc` that takes a list of resources as input and returns a list of security groups that exist within the default virtual private cloud (VPC). Each resource in the input list is expected to be a dictionary containing a 'vpc_id' key. The function should identify the default VPC ID using the `get_default_vpc_id` method and filter the resources based on this ID.
"""

def process(resources, default_vpc_id):
    default_vpc_security_groups = []

    for resource in resources:
        if 'vpc_id' in resource and resource['vpc_id'] == default_vpc_id:
            default_vpc_security_groups.append(resource)

    return default_vpc_security_groups