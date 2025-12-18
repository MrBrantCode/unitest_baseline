"""
QUESTION:
Create a function "avg_grade" that takes the total sum of grades and the length of the list as input, and returns the average of the grades. The grades are integers ranging from 0 to 100. The function should have a time complexity of O(1) and should not use any built-in functions or libraries for calculating the average.
"""

def avg_grade(total_sum_of_grades, length_of_list):
    average = total_sum_of_grades / length_of_list
    return average