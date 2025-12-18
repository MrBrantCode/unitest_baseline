"""
QUESTION:
Create a function called `find_perfect_numbers` that takes an integer `n` as input and returns a list of all perfect numbers up to `n`. A perfect number is a positive integer that is equal to the sum of its positive divisors excluding the number itself.
"""

def find_perfect_numbers(n):
    perfect_numbers = []
    for num in range(1, n+1):
        divisors = [i for i in range(1, num) if num%i == 0]
        if sum(divisors) == num:
           perfect_numbers.append(num)
    return perfect_numbers