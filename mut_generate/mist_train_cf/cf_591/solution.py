"""
QUESTION:
Write a function `find_most_common_element` that takes a list of integers as input and returns the most common element in the list. The function should have a time complexity of O(n) and should not use any built-in functions or methods that directly solve the problem. If there are multiple elements with the highest frequency, return any one of them. The input list will contain at least one element and at most 10^6 elements, and can contain negative numbers.
"""

def find_most_common_element(nums):
    """
    This function finds the most common element in a given list of integers.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The most common element in the list.

    """
    # Create an empty dictionary to store the frequencies of each element
    freq_dict = {}

    # Iterate through the elements of the list
    for num in nums:
        # If the element is already in the dictionary, increment its frequency by 1
        if num in freq_dict:
            freq_dict[num] += 1
        # If the element is not in the dictionary, add it with a frequency of 1
        else:
            freq_dict[num] = 1

    # Initialize the maximum frequency as 0 and the most common element as None
    max_freq = 0
    most_common = None

    # Iterate through the items of the dictionary
    for num, freq in freq_dict.items():
        # If the frequency is greater than the maximum frequency, update the maximum frequency and the most common element
        if freq > max_freq:
            max_freq = freq
            most_common = num

    # Return the most common element
    return most_common