"""
QUESTION:
Write a function named `transform_to_dict` that takes a list of strings as input and returns a dictionary where each key is a string from the list and its corresponding value is the sum of the ASCII values of all characters in the string. The function should handle any exceptions that may occur during the process.
"""

def transform_to_dict(input_list):
    """
    This function takes a list of strings as input and returns a dictionary 
    where each key is a string from the list and its corresponding value is 
    the sum of the ASCII values of all characters in the string.

    Args:
        input_list (list): A list of strings.

    Returns:
        dict: A dictionary where each key is a string from the list and its 
        corresponding value is the sum of the ASCII values of all characters 
        in the string.
    """
    try:
        return {elem: sum(ord(char) for char in elem) for elem in input_list}
    except Exception as e:
        print("An error occurred:", e)
        return None