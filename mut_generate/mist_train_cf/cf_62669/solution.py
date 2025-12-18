"""
QUESTION:
Create a feature to represent downtime in a model that predicts energy consumption. Consider the following two options: 

- Total Downtime: the total time lost due to power outage, machine failure, maintenance, etc.
- Downtime as a percentage of Total Planned Runtime: calculated as Downtime/Total Planned Runtime.

What are the key considerations when choosing between these two features, and which one is more helpful for interpreting and deriving action items for the business?
"""

def calculate_downtime_features(total_downtime, total_planned_runtime):
    """
    Calculate total downtime and downtime as a percentage of total planned runtime.

    Args:
        total_downtime (float): Total time lost due to power outage, machine failure, maintenance, etc.
        total_planned_runtime (float): Total planned runtime of the machine.

    Returns:
        tuple: A tuple containing total downtime and downtime as a percentage of total planned runtime.
    """

    # Calculate downtime as a percentage of total planned runtime
    # To avoid division by zero, we check if total planned runtime is zero
    downtime_percentage = (total_downtime / total_planned_runtime) * 100 if total_planned_runtime != 0 else 0

    return total_downtime, downtime_percentage