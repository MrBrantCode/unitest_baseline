"""
QUESTION:
Create a function `find_most_common` that takes a list of integers as input, and returns the most common positive integer in the list, excluding any duplicates. If there are multiple integers with the same highest frequency, any of them can be returned. If the input list is empty or contains no positive integers, the function should return `None`.
"""

def find_most_common(lst):
    """
    This function finds the most common positive integer in a list, excluding any duplicates.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    int or None: The most common positive integer in the list. If the input list is empty or contains no positive integers, it returns None.
    """
    freq_count = {}
    for num in lst:
        if num > 0:
            if num not in freq_count:
                freq_count[num] = 1
            else:
                freq_count[num] += 1
    
    sorted_freq_count = sorted(freq_count.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_freq_count:
        return sorted_freq_count[0][0]
    else:
        return None