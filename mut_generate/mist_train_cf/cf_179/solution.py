"""
QUESTION:
Write a function named `find_most_frequent` that finds the most frequent item in an array of integers and returns this item. The function should have a time complexity of O(n), where n is the length of the array, and should use constant space complexity, without using any built-in sorting or counting functions/methods. The array will contain at least one element and will not be sorted.
"""

def find_most_frequent(nums):
    """
    Finds the most frequent item in an array of integers.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The most frequent item in the array.
    """
    count = {}
    max_count = 0
    max_item = None

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

        if count[num] > max_count:
            max_count = count[num]
            max_item = num

    return max_item