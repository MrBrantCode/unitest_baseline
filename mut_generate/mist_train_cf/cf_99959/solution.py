"""
QUESTION:
Write a function `classify_data_points` that takes a list of tuples `data_points` where each tuple contains a numerical value `x` and a binary value `y`. The function should return a dictionary containing the count of data points classified as "A" and "B", where data points are classified as "A" if `x` is greater than 10 and `y` is 0, and as "B" otherwise.
"""

def classify_data_points(data_points):
    a_count = len(list(filter(lambda x: x[0] > 10 and x[1] == 0, data_points)))
    b_count = len(data_points) - a_count
    return {"A": a_count, "B": b_count}