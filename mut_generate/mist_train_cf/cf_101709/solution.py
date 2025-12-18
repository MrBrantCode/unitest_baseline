"""
QUESTION:
Create a function named classify_data_points that takes a list of tuples (x, y), where x is a numerical value and y is a binary value. The function should classify the data points based on the following rule: if x is greater than 10 and y is 0, classify as "A", otherwise classify as "B". The function should return a dictionary containing the count of data points classified as "A" and "B".
"""

def classify_data_points(data_points):
    a_count = len(list(filter(lambda x: x[0] > 10 and x[1] == 0, data_points)))
    b_count = len(data_points) - a_count
    return {"A": a_count, "B": b_count}