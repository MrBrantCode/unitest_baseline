"""
QUESTION:
Create a function called `calculate_mean` that takes a list of numbers as input and returns the mean of the data set as a float rounded to two decimal places. The input list is guaranteed to have exactly 10 elements.
"""

def calculate_mean(data_set):
    return round(sum(data_set) / len(data_set), 2)