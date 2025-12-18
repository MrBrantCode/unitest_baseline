"""
QUESTION:
Implement a function called `loop_through_list` that demonstrates different methods to loop through a list in Python, including a for loop, while loop, list comprehension, and map() function. The function should take a list as an argument and return the looped elements.
"""

def loop_through_list(input_list):
    """
    This function demonstrates different methods to loop through a list in Python.
    
    Parameters:
    input_list (list): The input list to be looped through.
    
    Returns:
    A list with the looped elements.
    """
    
    # Using a for loop
    for_loop_result = [element for element in input_list]
    
    # Using a while loop
    i = 0
    while_loop_result = []
    while i < len(input_list):
        while_loop_result.append(input_list[i])
        i += 1
    
    # Using list comprehension
    list_comprehension_result = [element for element in input_list]
    
    # Using map() function
    map_result = list(map(lambda x: x, input_list))
    
    # Combine the results from all the methods
    result = [for_loop_result, while_loop_result, list_comprehension_result, map_result]
    
    return result