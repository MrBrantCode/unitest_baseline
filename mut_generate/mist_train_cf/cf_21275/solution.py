"""
QUESTION:
Find the two maximum numbers in a list of integers without using any comparison operator. The function `find_two_max` should take a list of integers as input and return a list containing the two maximum numbers. The function should have a time complexity of O(n), a space complexity of O(1), and should not modify the original list.
"""

def find_two_max(nums):
    """
    Find the two maximum numbers in a list of integers without using any comparison operator.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A list containing the two maximum numbers.

    """
    # Initialize max1 and max2 with the smallest possible integer value
    max1 = float('-inf')
    max2 = float('-inf')

    # Iterate through the list of integers
    for num in nums:
        # If num is greater than max1, update max2 with the current value of max1 and update max1 with num
        if num > max1:
            max2 = max1
            max1 = num
        # If num is less than max1 but greater than max2, update max2 with num
        elif num > max2:
            max2 = num

    # Return [max1, max2] as the result
    return [max1, max2]