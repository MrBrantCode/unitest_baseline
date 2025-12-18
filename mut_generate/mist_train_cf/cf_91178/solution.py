"""
QUESTION:
Create a function "avg_grade" that takes the total sum of grades and the length of the list as input, and returns the average of the grades. The function should have a time complexity of O(1) and should not use any built-in functions or libraries to calculate the average. The total sum and length of the list will be pre-calculated separately before calling the function.
"""

def avg_grade(grades_sum, length):
    average = grades_sum / length
    return average