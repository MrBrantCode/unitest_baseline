"""
QUESTION:
Create a function called `ascii_sum_dict` that takes a list of strings as input and returns a dictionary where the keys are the elements of the list and the values are the sum of their ASCII values. The function should handle any exceptions that may occur during the process.
"""

def ascii_sum_dict(lst):
    """
    This function takes a list of strings as input and returns a dictionary 
    where the keys are the elements of the list and the values are the sum 
    of their ASCII values.

    Args:
        lst (list): A list of strings.

    Returns:
        dict: A dictionary where keys are the input strings and values are 
              the sum of their ASCII values.

    Raises:
        Exception: If any exception occurs during the process.
    """
    try:
        return {elem: sum(ord(char) for char in elem) for elem in lst}
    except Exception as e:
        print("An error occurred:", e)
        return None