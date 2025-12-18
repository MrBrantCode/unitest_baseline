"""
QUESTION:
Create a function named `count_elements` that takes a list of strings as input and returns the total number of elements in the list. You must use a for loop to iterate over the elements and increment a counter variable for each element. You are not allowed to use the built-in len() function or any other built-in function that counts the number of elements.
"""

def count_elements(mylist):
    """
    This function counts the total number of elements in a list of strings.
    
    Parameters:
    mylist (list): A list of strings.
    
    Returns:
    int: The total number of elements in the list.
    """
    counter = 0
    for element in mylist:
        counter += 1
    return counter