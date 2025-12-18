"""
QUESTION:
Create a function named `avg_three_max_min` that takes a list of integers as input and returns the arithmetic average of the three highest and three lowest integers in the list. The input list must have at least six elements.
"""

def avg_three_max_min(numbers):
    # Sorting the list in ascending order
    numbers.sort()

    # Getting the three lowest and three highest numbers
    three_lowest = numbers[:3]
    three_highest = numbers[-3:]

    # Calculating the average
    avg = sum(three_lowest + three_highest) / 6

    return avg