"""
QUESTION:
Write a function `calculate_salary` that calculates an employee's salary after a certain number of years with annual raises. The function should take four parameters: the initial salary `P`, the annual raise percentage `r` (as a decimal), the number of times the salary is raised per year `n`, and the number of years `t`. The function should return the final salary after `t` years, taking into account compounded annual salary increments.
"""

def calculate_salary(P, r, n, t):
    A = P * (1 + r/n) ** (n*t)
    return A