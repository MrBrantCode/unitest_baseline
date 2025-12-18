"""
QUESTION:
Create a function "avg_grade" that takes a list of grades as input and returns the average grade. The function must have a time complexity of O(n), where n is the number of grades, and cannot use any built-in functions or libraries. The input list will only contain integers between 0 and 100, and the function should raise an exception if the list is empty or if it contains any negative values.
"""

def avg_grade(grades):
    if len(grades) == 0:
        raise Exception("List of grades is empty.")
    
    sum_grades = 0
    for grade in grades:
        if grade < 0:
            raise Exception("List of grades contains negative values.")
        sum_grades += grade
    
    return sum_grades / len(grades)