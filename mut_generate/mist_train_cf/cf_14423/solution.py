"""
QUESTION:
Write a function `count_distinct_salaries` that takes a table of employee salaries as input and returns the count of distinct salaries greater than $50,000. The table is represented as a list of integers where each integer is an employee's salary.
"""

def count_distinct_salaries(salaries):
    return len(set([salary for salary in salaries if salary > 50000]))