"""
QUESTION:
Create a function called `specialFilter` that takes an array of numbers as input. Return the count of elements in the array where the absolute value is greater than 10 and both the first and last digits are odd.
"""

def specialFilter(numbers):
    count = 0
    for number in numbers:
        if abs(number) > 10 and str(abs(number))[0] in "13579" and str(abs(number))[-1] in "13579":
            count += 1
    return count