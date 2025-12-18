"""
QUESTION:
Create a function called `find_second_largest` that takes a list of integers as input and returns the second largest number in the list. The function should only consider positive integers less than 100 and ignore any negative numbers. If the list is empty, contains less than two positive integers less than 100, or contains duplicate largest numbers, the function should return an error message. If the list contains no positive integers less than 100, the function should also return an error message.
"""

def find_second_largest(num_list):
    """
    This function takes a list of integers as input and returns the second largest number in the list.
    The function only considers positive integers less than 100 and ignores any negative numbers.
    If the list is empty, contains less than two positive integers less than 100, 
    or contains duplicate largest numbers, the function returns an error message.

    Parameters:
    num_list (list): A list of integers.

    Returns:
    int: The second largest number in the list, or an error message if conditions are not met.
    """

    # Filter the list to include only positive integers less than 100
    valid_numbers = [num for num in num_list if num > 0 and num < 100]
    
    # Check if the list contains at least two positive integers less than 100
    if len(valid_numbers) < 2:
        return "Error: List should contain at least two positive integers less than 100."
    
    # Convert the list to a set to remove duplicates
    unique_numbers = set(valid_numbers)
    
    # Check if the list contains at least one positive integer less than 100
    if len(unique_numbers) == 0:
        return "Error: List should contain at least one positive integer less than 100."
    
    # Find the maximum number in the list
    max_num = max(unique_numbers)
    
    # Check if the maximum number is a duplicate
    if valid_numbers.count(max_num) > 1:
        return "Error: No second largest number exists due to duplicate largest numbers."
    
    # Remove the maximum number from the set
    unique_numbers.remove(max_num)
    
    # Find the second largest number in the list
    second_largest_num = max(unique_numbers)
    
    return second_largest_num