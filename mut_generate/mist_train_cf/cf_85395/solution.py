"""
QUESTION:
Implement a function called `tuple_sum` that sorts a list of integer tuples in ascending order based on the sum of the tuple's elements. If the sum of the tuple's elements is the same, arrange them based on the first element in the tuple.
"""

def tuple_sum(t):
    return (sum(t), t[0])