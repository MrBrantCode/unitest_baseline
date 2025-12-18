"""
QUESTION:
Create a function named `divide_pairs` that takes a list of pairs of numbers as input, divides the first number in each pair by the second number, and returns the results in a new list. If a division by zero occurs, append "Error: Division by Zero" to the result list instead.
"""

def divide_pairs(pair_list):
    result = []
    for pair in pair_list:
        try:
            result.append(pair[0]/pair[1])
        except ZeroDivisionError:
            result.append("Error: Division by Zero")
    return result