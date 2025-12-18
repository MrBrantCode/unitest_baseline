"""
QUESTION:
Write a SQL query to calculate and return the average grade of all students from the 'Students' table. The 'Students' table contains 'name' and 'grade' columns. The query should be a modification of the original query: SELECT name, grade FROM Students;.
"""

def calculate_average_grade(grades):
    return sum(grades) / len(grades)