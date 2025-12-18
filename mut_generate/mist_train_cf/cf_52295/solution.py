"""
QUESTION:
Create a function `find_occurrences` that takes a list of integers and a variable number of integer arguments. The function should return a dictionary where each key is a unique integer from the arguments and the corresponding value is a list of indices where that integer appears in the list. If an integer from the arguments does not appear in the list, the value should be an empty list.
"""

def find_occurrences(arr, *args):
    d = {}
    for num in args:
        if num in arr:
            d[num] = [i for i, n in enumerate(arr) if n == num]
        else:
            d[num] = []
    return d