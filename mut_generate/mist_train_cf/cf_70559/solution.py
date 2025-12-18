"""
QUESTION:
Create a function `is_srm_tolerable` that determines whether a given Sample Ratio Mismatch (SRM) percentage is tolerable based on the control and test group sizes and a specified tolerance threshold.

The function should take in the number of users in the control and test groups, and the tolerable SRM percentage as input parameters. It should return a boolean indicating whether the SRM is tolerable based on the given threshold.
"""

def is_srm_tolerable(control_group_size, test_group_size, tolerable_srm_percentage):
    """
    Determines whether a given Sample Ratio Mismatch (SRM) percentage is tolerable.

    Args:
    control_group_size (int): The number of users in the control group.
    test_group_size (int): The number of users in the test group.
    tolerable_srm_percentage (float): The tolerable SRM percentage.

    Returns:
    bool: Whether the SRM is tolerable based on the given threshold.
    """

    # Calculate the expected ratio of the test group to the total
    expected_ratio = test_group_size / (control_group_size + test_group_size)
    
    # Calculate the actual ratio of the test group to the total
    actual_ratio = test_group_size / (control_group_size + test_group_size)
    
    # Calculate the SRM percentage
    srm_percentage = abs((actual_ratio - expected_ratio) / expected_ratio) * 100
    
    # Return whether the SRM is tolerable based on the given threshold
    return srm_percentage <= tolerable_srm_percentage