"""
QUESTION:
Write a function called `sum_and_avg` that takes three numbers as arguments, calculates and returns their sum and average. The average should be rounded to two decimal places.
"""

def sum_and_avg(num1, num2, num3):
    total = num1 + num2 + num3
    avg = round(total / 3, 2)
    return total, avg