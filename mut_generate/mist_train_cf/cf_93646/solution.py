"""
QUESTION:
Create a function called `find_armstrong_numbers` that takes two parameters, `start` and `end`, representing a range of numbers. The function should return a list of all Armstrong numbers within the given range, as well as their sum. An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits. For example, 371 is an Armstrong number since 3*3*3 + 7*7*7 + 1*1*1 = 371. The function should only consider positive integers within the given range and should return the list of Armstrong numbers and their sum.
"""

def find_armstrong_numbers(start, end):
    def is_armstrong_number(number):
        num_str = str(number)
        n = len(num_str)
        armstrong_sum = sum(int(digit)**n for digit in num_str)
        return armstrong_sum == number

    armstrong_numbers = [number for number in range(start, end+1) if is_armstrong_number(number)]
    return armstrong_numbers, sum(armstrong_numbers)