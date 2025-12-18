"""
QUESTION:
Create a function named `find_largest` that takes a list `arr` as input and returns the largest numeric value. The function should handle non-numeric inputs by skipping them and continue searching for the largest numeric value. The function should return the largest integer value found in the list. If the list is empty or does not contain any numeric values, the function's behavior is undefined.
"""

def find_largest(arr):
    largest = None
    for item in arr:
        try:
            num = int(item) # Attempt to convert the item into an integer.
        except ValueError: # If a ValueError occurs, skip this item.
            continue
        if largest is None or num > largest:
            largest = num
    return largest