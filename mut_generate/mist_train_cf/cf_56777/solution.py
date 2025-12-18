"""
QUESTION:
Design a function called `find_odd_occur` that takes an array of integers as input and returns a list of elements that occur an odd number of times in the array. The function should have a time complexity of O(n) and space complexity of O(n), where n is the size of the array.
"""

def find_odd_occur(arr):
    """
    This function takes an array of integers as input and returns a list of elements that occur an odd number of times in the array.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A list of integers that occur an odd number of times in the input array.
    """

    # Create an empty hash map
    map = {}
  
    # Store counts of all elements in the hash map
    for i in range(len(arr)):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1

    # Store all elements for which count is odd
    result = []
    for ele in map:
        if map[ele] % 2 != 0:
            result.append(ele)

    return result