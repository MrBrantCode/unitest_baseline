"""
QUESTION:
Create a function `sort_and_sum(lst)` that takes a list of integers as input, sorts the list in descending order, excludes all even numbers from the sorted list, and returns the sum of the remaining numbers. The function should run in O(nlogn) time complexity.
"""

def sort_and_sum(lst):
    """
    This function takes a list of integers, sorts the list in descending order, 
    excludes all even numbers from the sorted list, and returns the sum of the remaining numbers.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The sum of the remaining numbers after excluding even numbers from the sorted list.
    """
    # Sort the list in descending order
    sorted_lst = sorted(lst, reverse=True)
    
    # Exclude all even numbers from the sorted list
    filtered_lst = [num for num in sorted_lst if num % 2 != 0]
    
    # Calculate the sum of the remaining numbers
    total_sum = sum(filtered_lst)
    
    return total_sum