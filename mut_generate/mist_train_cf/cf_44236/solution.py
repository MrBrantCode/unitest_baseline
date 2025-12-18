"""
QUESTION:
Write a function `solution(lst)` that takes a list of integers `lst` as input. The function should calculate the sum of all odd elements located at even indices in the list and return this sum along with a list of these odd elements and their corresponding even indices.
"""

def solution(lst):
    """
    Calculate the sum of all odd elements located at even indices in the list.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    tuple: A tuple containing the sum of odd elements at even indices and a list of these odd elements along with their indices.
    """
    odd_sum = 0
    odd_list = []
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            odd_sum += lst[i]
            odd_list.append((i, lst[i]))
    return odd_sum, odd_list