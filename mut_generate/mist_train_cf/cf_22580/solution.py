"""
QUESTION:
Create a function called `reverse_sort_strings` that takes a list of strings as input. Remove any duplicate strings from the list, then sort the unique strings in descending order of their lengths. Convert the sorted list to all uppercase letters and return the result. The time complexity of the function should be O(n log n) where n is the length of the input list.
"""

def reverse_sort_strings(strings):
    # Remove duplicates and sort by reverse length
    unique_strings = sorted(set(strings), key=len, reverse=True)
    
    # Convert to uppercase
    return [string.upper() for string in unique_strings]