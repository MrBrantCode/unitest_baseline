"""
QUESTION:
Write a function called `find_integer` that takes two arguments: a multi-dimensional array of integers and a target integer. The function should return the total number of occurrences of the target integer in the array.
"""

def find_integer(array, num):
    count = 0
    for el in array:
        if isinstance(el, list):
            count += find_integer(el, num)
        else:
            if el == num:
                count += 1
    return count