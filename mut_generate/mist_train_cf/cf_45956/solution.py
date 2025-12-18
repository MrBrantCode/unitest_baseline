"""
QUESTION:
Find a unique pair of distinct numbers in a given set of decimal numbers such that one number divided by the other equals a predetermined quotient.
"""

def find_pair(nums, quotient):
    """
    Find a unique pair of distinct numbers in a given set of decimal numbers 
    such that one number divided by the other equals a predetermined quotient.

    Args:
        nums (list): A list of decimal numbers.
        quotient (float): The predetermined quotient.

    Returns:
        tuple: A tuple of two distinct numbers if found, otherwise None.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] / nums[j] == quotient or nums[j] / nums[i] == quotient:
                return (nums[i], nums[j])
    return None