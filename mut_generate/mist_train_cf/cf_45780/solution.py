"""
QUESTION:
Write a function named `remove_and_calculate_mean` that takes a list of numbers and a number to be removed as parameters. The function should return a dictionary where keys are indexes of the original list (excluding those pointing to the number to be removed) and values are the corresponding numbers, and the mean of the remaining numbers. The function should exclude the number to be removed from the dictionary and the mean calculation.
"""

def remove_and_calculate_mean(mylist, num_to_remove):
    """
    This function takes a list of numbers and a number to be removed as parameters.
    It returns a dictionary where keys are indexes of the original list (excluding those pointing to the number to be removed) 
    and values are the corresponding numbers, and the mean of the remaining numbers.
    
    Parameters:
    mylist (list): The list of numbers.
    num_to_remove (int): The number to be removed from the list.
    
    Returns:
    tuple: A dictionary with indexes and corresponding numbers, and the mean of the remaining numbers.
    """
    # Remove all instances of 'num_to_remove' and transform to dictionary
    mydict = {i:val for i, val in enumerate(mylist) if val != num_to_remove}

    # Calculate the mean of remaining numbers
    mean = sum(mydict.values())/len(mydict) if mydict else 0  # Avoid division by zero

    return mydict, mean