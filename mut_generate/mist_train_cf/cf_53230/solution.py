"""
QUESTION:
Write a function `average_tuples` that takes a tuple of tuples, each containing integers, and returns a list of the average value for each tuple. If a tuple contains non-integer values, the function should return an error message for that specific tuple instead of its average.
"""

def average_tuples(tuples):
    averages = []
    for t in tuples:
        try:
            sum_val = sum(t)
            averages.append(sum_val / len(t))
        except TypeError:
            averages.append('Error: Non-integer values in tuple')
    return averages