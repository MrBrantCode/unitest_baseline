"""
QUESTION:
Create a function called `process_list` that takes a list of items as input, removes non-string items from the end of the list using the `pop()` operation, and returns the updated list along with a list of removed non-string items. The function should iterate through the input list from the end to the beginning and validate the type of each item before removal.
"""

def process_list(arr):
    removed = []
    i = len(arr) - 1
    while i >= 0:
        if type(arr[i]) is not str:
            removed.append(arr.pop(i))
        i -= 1
    return arr, removed