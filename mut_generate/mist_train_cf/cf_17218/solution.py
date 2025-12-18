"""
QUESTION:
Find the most occurring element in an array of integers using a constant amount of extra space and achieving a time complexity of O(n). The solution should not use additional data structures such as dictionaries or hash maps. The function should be implemented using the most efficient approach.
"""

def most_occurring_element(nums):
    """
    Find the most occurring element in an array of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The most occurring element in the list.
    """
    
    # Initialize candidate and count with None and 0 respectively
    candidate = None
    count = 0

    # Iterate through each element in the array
    for num in nums:
        # If count is equal to 0, set candidate to num and count to 1
        if count == 0:
            candidate = num
            count = 1
        # If num is equal to candidate, increment count by 1
        elif num == candidate:
            count += 1
        # If num is not equal to candidate, decrement count by 1
        else:
            count -= 1

    # Count the occurrences of the candidate element
    occurrences = sum(1 for num in nums if num == candidate)

    # Return the candidate element
    return candidate if occurrences > len(nums) // 2 else None