"""
QUESTION:
Function: `handle_provisioned_throughput_exceeded`

Your function should handle the 'ProvisionedThroughputExceededException' error in Amazon DynamoDB by managing the provisioned throughput capacity. The function should take the current read capacity units (RCUs) and write capacity units (WCUs) as input and return the adjusted RCUs and WCUs to prevent the exception. The function should also consider the upper and lower limits of the provisioned throughput capacity to prevent overuse or underuse of resources. 

The function should be able to adjust the provisioned throughput capacity based on the current capacity usage and traffic patterns. It should also be able to leverage DynamoDB's auto-scaling feature to automatically adjust the table's capacity.
"""

def handle_provisioned_throughput_exceeded(current_rcu, current_wcu, lower_limit_rcu, upper_limit_rcu, lower_limit_wcu, upper_limit_wcu):
    """
    Handle the 'ProvisionedThroughputExceededException' error in Amazon DynamoDB by managing the provisioned throughput capacity.

    Args:
        current_rcu (int): The current read capacity units.
        current_wcu (int): The current write capacity units.
        lower_limit_rcu (int): The lower limit of the read capacity units.
        upper_limit_rcu (int): The upper limit of the read capacity units.
        lower_limit_wcu (int): The lower limit of the write capacity units.
        upper_limit_wcu (int): The upper limit of the write capacity units.

    Returns:
        tuple: A tuple containing the adjusted read capacity units and write capacity units.
    """

    # Calculate the new read capacity units, increasing by 50% if it's below the upper limit
    new_rcu = min(current_rcu * 1.5, upper_limit_rcu)
    # Ensure the new read capacity units are not below the lower limit
    new_rcu = max(new_rcu, lower_limit_rcu)

    # Calculate the new write capacity units, increasing by 50% if it's below the upper limit
    new_wcu = min(current_wcu * 1.5, upper_limit_wcu)
    # Ensure the new write capacity units are not below the lower limit
    new_wcu = max(new_wcu, lower_limit_wcu)

    return new_rcu, new_wcu