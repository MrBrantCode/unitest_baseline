"""
QUESTION:
Assessing the contribution of each error source to the overall accuracy in a robotic system.

Create a function `assess_error_contribution` that calculates the contribution of each error source to the overall accuracy in a robotic system. The function should take the variances of the error distributions associated with each source as input and return the significance of each error source as a percentage.

Restrictions: The error sources are independent, and their individual variances are known.
"""

def assess_error_contribution(variances):
    """
    Calculate the contribution of each error source to the overall accuracy in a robotic system.

    Parameters:
    variances (list): A list of variances of the error distributions associated with each source.

    Returns:
    list: A list of the significance of each error source as a percentage.
    """
    total_variance = sum(variances)
    if total_variance == 0:
        return [0] * len(variances)
    
    contributions = [variance / total_variance * 100 for variance in variances]
    return contributions