"""
QUESTION:
Create a function called `create_array` that generates an array of integers ranging from 0 to a specified limit (inclusive) and returns the array. The limit will be 20 in this case. The function should not take any arguments other than the limit, which will be passed to it.
"""

def create_array(limit):
    array = []
    for i in range(0, limit + 1):
        array.append(i)
    return array

# or in a more pythonic way
def create_array(limit):
    return list(range(limit + 1))