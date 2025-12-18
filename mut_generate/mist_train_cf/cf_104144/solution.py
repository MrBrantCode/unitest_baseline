"""
QUESTION:
Create a function `average_of_digit_sums` that takes three integers as input and returns the average of the sum of their digits. The function should handle any non-negative integers.
"""

def average_of_digit_sums(num1, num2, num3):
    # Calculate the sum of the digits for each number
    sum1 = sum(int(d) for d in str(num1))
    sum2 = sum(int(d) for d in str(num2))
    sum3 = sum(int(d) for d in str(num3))

    # Calculate the average of the sums
    average = (sum1 + sum2 + sum3) / 3
    return average