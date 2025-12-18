"""
QUESTION:
Create a function called `subtract_lists` that takes two lists of integers as arguments, each with a length from 1 to 10^3 and containing integers from -10^3 to 10^3. The function should return a list of the element-wise subtraction of the second list from the first. If the lists are not of the same length, return an error message. If the lists contain non-numeric values, handle the error gracefully and return an appropriate error message.
"""

def subtract_lists(list1, list2):
    # Check if both lists have the same length
    if len(list1) != len(list2):
        return "Error: Lists are not of the same length."

    # Subtract each pair of elements
    try:
        result = [a - b for a, b in zip(list1, list2)]
    except TypeError as err:
        return f"Error: Lists must contain only numbers. {err}"

    return result