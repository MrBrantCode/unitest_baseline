"""
QUESTION:
Implement a function `loop_through_dict` that takes a dictionary as input and demonstrates three different ways of looping through it: traditional loop constructs, dictionary comprehensions, and the map() function. The function should filter the dictionary for values greater than 2, create a new dictionary with increased values, and return the original dictionary, filtered dictionary, and new dictionary.
"""

def loop_through_dict(input_dict):
    """
    This function demonstrates three different ways of looping through a dictionary:
    traditional loop constructs, dictionary comprehensions, and the map() function.
    
    It filters the dictionary for values greater than 2, creates a new dictionary with increased values,
    and returns the original dictionary, filtered dictionary, and new dictionary.
    
    Parameters:
    input_dict (dict): The input dictionary to be processed.
    
    Returns:
    tuple: A tuple containing the original dictionary, filtered dictionary, and new dictionary.
    """
    
    # Traditional Loop Constructs
    for key, value in input_dict.items():
        # We're simply using a for loop to iterate over each (key, value) pair in the dictionary
        pass  # We don't need to print anything here
    
    # Dictionary Comprehensions
    filtered_dict = {key: value for key, value in input_dict.items() if value > 2}
    # We're creating a new dictionary that only includes the entries from the original dictionary 
    # where the value is greater than 2
    
    # map() Function
    new_dict = dict(map(lambda item: (item[0], item[1] + 1), input_dict.items()))
    # We're using a lambda function to create a new dictionary where every value is increased by 1
    
    return input_dict, filtered_dict, new_dict