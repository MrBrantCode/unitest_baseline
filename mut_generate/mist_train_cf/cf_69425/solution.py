"""
QUESTION:
Implement a function named `process_list` that takes a list and a callback function as input. The function should iterate through the list, apply the callback function to each element, and return the results in a new list while maintaining the original order. The function must handle exceptions raised by the callback function.
"""

def process_list(input_list, callback):
    """
    Applies a callback function to each element in the input list and returns the results.
    
    Args:
        input_list (list): The list of elements to process.
        callback (function): The function to apply to each element.
    
    Returns:
        list: A new list containing the results of applying the callback function to each element.
    """
    result = []
    for element in input_list:
        try:
            result.append(callback(element))
        except Exception as e:
            print(f"Error processing {element}: {e}")
    return result