"""
QUESTION:
Write a function `longest_common_substring` that takes two lists of integers as input and returns the product of their longest common substring that is a strictly increasing subsequence and has a length of at least 5. If there are multiple longest common substrings, return the product of the one that starts at the earliest index in the first list. If no such common substring exists, return -1.
"""

def longest_common_substring(list1, list2):
    """
    This function calculates the product of the longest common substring 
    that is a strictly increasing subsequence and has a length of at least 5 
    from two input lists of integers.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        int: The product of the longest common substring. If no such common substring exists, returns -1.
    """

    max_length = 0
    start_index = 0

    for i in range(len(list1)):
        for j in range(len(list2)):
            length = 0
            while (i+length < len(list1)) and (j+length < len(list2)) and (list1[i+length] == list2[j+length]):
                length += 1
            
            if length >= 5 and length > max_length:
                max_length = length
                start_index = i
    
    if max_length == 0:
        return -1
    
    common_substring = list1[start_index:start_index+max_length]
    product = 1
    for num in common_substring:
        product *= num
    
    return product