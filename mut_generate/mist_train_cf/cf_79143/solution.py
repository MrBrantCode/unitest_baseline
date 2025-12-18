"""
QUESTION:
Create a function named `nested_dictionary` that takes a list of tuples as input, where each tuple contains two elements. The function should return a nested dictionary where the first element of each tuple is the key to the external dictionary, the second element is the key to the respective nested dictionary, and the values of the nested dictionary are the square and cube of the second element of the tuple. The nested dictionary should have exactly two keys: 'square' and 'cube'.
"""

def nested_dictionary(tuples):
    """
    This function takes a list of tuples as input and returns a nested dictionary.
    
    Parameters:
    tuples (list): A list of tuples where each tuple contains two elements.
    
    Returns:
    dict: A nested dictionary where the first element of each tuple is the key to the external dictionary,
          the second element is the key to the respective nested dictionary, and the values of the nested dictionary
          are the square and cube of the second element of the tuple.
    """
    return {i: {j: {'square': j**2, 'cube': j**3}} for i, j in tuples}