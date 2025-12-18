"""
QUESTION:
Create a function called `sort_based_on_number` that sorts an array of strings containing both letters and numbers in descending order based on the numerical part of each string. The numerical part is assumed to be at the start of the string.
"""

def sort_based_on_number(arr):
    # Define a custom sorting function that extracts the numeric part of each string
    def get_numeric_part(s):
        return int(''.join(filter(str.isdigit, s)))

    # Sort the array using the custom sorting function in descending order
    arr.sort(key=get_numeric_part, reverse=True)
    return arr