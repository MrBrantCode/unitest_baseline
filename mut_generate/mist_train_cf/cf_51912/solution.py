"""
QUESTION:
Write a function `tenth_largest` that takes a list of numbers as input, removes duplicates, and returns the 10th largest unique value. If the list has fewer than 10 unique values, return the error message "Error: Less than 10 unique values in the list". The function should not take any other parameters.
"""

def tenth_largest(lst):
    unique_list = list(set(lst))
    unique_list.sort(reverse=True)
    if len(unique_list) < 10:
        return "Error: Less than 10 unique values in the list"
    else:
        return unique_list[9]