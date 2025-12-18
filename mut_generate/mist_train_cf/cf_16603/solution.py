"""
QUESTION:
Create a function "avg_grade" that calculates the average of a given list of grades. The function should take a list of integers ranging from 0 to 100 as input and return their average as a floating-point number. If the input list is empty, the function should raise an exception. Additionally, if the list contains any negative values, the function should raise an exception. The function should not use any built-in functions or libraries and should achieve a time complexity of O(n), where n is the number of grades in the list.
"""

def calculate_average(grades):
    if len(grades) == 0:
        raise Exception("List of grades is empty.")
    
    sum_grades = 0
    for grade in grades:
        if grade < 0 or grade > 100:
            raise Exception("List of grades contains values out of range.")
        sum_grades += grade
    
    return sum_grades / len(grades)