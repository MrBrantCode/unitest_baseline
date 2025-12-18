"""
QUESTION:
Create a function called `remove_non_repeating_elements` that takes an array of integers as input, and returns a new array containing the elements that occur more than once in the input array, while preserving their original order. The function should not modify the input array and should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input array.
"""

def remove_non_repeating_elements(arr):
    """
    This function takes an array of integers as input and returns a new array containing 
    the elements that occur more than once in the input array, while preserving their 
    original order.

    Parameters:
    arr (list): The input array of integers.

    Returns:
    list: A new array containing the elements that occur more than once in the input array.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = {}
    result = []

    # Count the occurrences of each element in the input array
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Append only the elements that occur more than once to the result array
    for num in arr:
        if count[num] > 1:
            result.append(num)

    return result