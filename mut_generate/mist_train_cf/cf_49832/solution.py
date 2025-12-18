"""
QUESTION:
Write a function named `calculate_unique_instances` that takes as input four variables with possible values of 3, 2, 2, 2 and 3 categorization results. The function should calculate the maximum number of unique instances that can be generated under these circumstances.
"""

def calculate_unique_instances(var1, var2, var3, var4, categorization_results):
    """
    Calculate the maximum number of unique instances that can be generated.

    Args:
        var1 (int): Number of possibilities for the first variable.
        var2 (int): Number of possibilities for the second variable.
        var3 (int): Number of possibilities for the third variable.
        var4 (int): Number of possibilities for the fourth variable.
        categorization_results (int): Number of categorization results.

    Returns:
        int: The maximum number of unique instances.
    """
    # Calculate the total number of unique instances for the variables
    unique_instances_variables = var1 * var2 * var3 * var4
    
    # Calculate the total number of unique instances taking into account categorization results
    total_unique_instances = unique_instances_variables * categorization_results
    
    return total_unique_instances