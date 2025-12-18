"""
QUESTION:
Implement a function called `square_mapper` that takes a list of integers as input and returns a new list containing the squares of each integer, without using any loops or list comprehensions. Use the `map` higher-order function to apply the squaring operation to each element in the input list.
"""

def square_mapper(input_list):
    def square(x):
        return x * x

    return list(map(square, input_list))