"""
QUESTION:
Implement a function `calculate_average_joins(JBD)` that takes a dictionary `JBD` as input, where each key represents a day of the week and each corresponding value is a list of integers representing the number of joins for that day. The function should return a new dictionary containing the average number of joins for each day of the week, calculated by summing up the number of joins for each day and dividing by the total number of values. The returned dictionary should have the same keys as the input dictionary, but with the average values.
"""

def calculate_average_joins(JBD):
    average_joins = {}
    for day, joins in JBD.items():
        average_joins[day] = sum(joins) / len(joins)
    return average_joins