"""
QUESTION:
Implement a function named `do_something` that takes a list of integers as input, removes any duplicate elements, and returns a sorted list of integers. The function must not use built-in sorting or duplicate removal methods. It should only return a sorted list of unique integers.
"""

def do_something(data):
    """
    This function removes any duplicate elements from the input list and returns a sorted list of unique integers.
    
    The function uses a simple iteration to remove duplicates and the bubble sort algorithm to sort the list.
    
    Args:
        data (list): A list of integers.
    
    Returns:
        list: A sorted list of unique integers.
    """
    # Remove duplicates
    unique_data = []
    for num in data:
        if num not in unique_data:
            unique_data.append(num)
    
    # Sort the list
    for i in range(len(unique_data)):
        for j in range(i+1, len(unique_data)):
            if unique_data[i] > unique_data[j]:
                unique_data[i], unique_data[j] = unique_data[j], unique_data[i]
    
    return unique_data