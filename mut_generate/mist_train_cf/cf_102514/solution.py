"""
QUESTION:
Implement a function named `process_list` that takes a list of integers as input, converts all negative elements to positive, removes any duplicates, and sorts the list in descending order. The function should return an empty list if the input is empty and handle non-numeric elements by returning an error message.
"""

def process_list(lst):
    try:
        if not lst:  
            return []

        lst = [abs(x) for x in lst]
        lst = list(set(lst))
        lst.sort(reverse=True)

        return lst

    except TypeError:
        return "Error: Non-numeric elements in the list"