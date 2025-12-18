"""
QUESTION:
Write a function `longest_consecutive_sequence(nums)` that takes a list of integers `nums` as input and returns the start and end indices of the longest consecutive sequence that is strictly increasing by exactly 1 and contains at least five elements. If no such sequence is found, return a corresponding message. The function should return the start and end indices as a list, where the first element is the start index and the second element is the end index. The sequence index should be based on the original input list.
"""

def longest_consecutive_sequence(nums):
    """
    This function finds the start and end indices of the longest consecutive sequence 
    that is strictly increasing by exactly 1 and contains at least five elements.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The start and end indices of the longest consecutive sequence. 
              If no such sequence is found, returns "No consecutive sequence found."
    """
    nums_set = set(nums)
    longest_seq = []
    max_length = 0

    for i, num in enumerate(nums):
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            if current_length > max_length and current_length >= 5:
                max_length = current_length
                longest_seq = [i, i + current_length - 1]

    if max_length >= 5:
        return longest_seq
    else:
        return "No consecutive sequence found."