"""
QUESTION:
Write a function named `odd_numbers` that takes a list of integers as input, returns a list of odd integers in descending order, handles exceptions for non-integer inputs by returning an error message, and efficiently handles large lists and negative numbers. The function should not include any irrelevant information or code snippets.
"""

def odd_numbers(lst):
    try:
        # Extract only the odd numbers from the list
        odd_lst = [i for i in lst if isinstance(i, int) and i % 2 == 1] 

        # Sort the odd numbers in descending order
        odd_lst.sort(reverse=True)

        return odd_lst
    except TypeError as te:
        # Handle non-integer inputs and outputs appropriate error message
        return f"Error occurred: {str(te)}. Please ensure all input items are integers."