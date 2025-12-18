"""
QUESTION:
Define a function `aggregate(arr)` that calculates the sum of all integers and concatenates all strings in the input array `arr`. The function should return two values: the sum of integers and the concatenation of strings. The input array can contain both integers and strings.
"""

def aggregate(arr):
    num_sum = 0
    str_sum = ''
    for element in arr:
        if isinstance(element, int):
            num_sum += element
        elif isinstance(element, str):
            str_sum += element
    return num_sum, str_sum