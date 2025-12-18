"""
QUESTION:
Write a function called `sum_of_even_numbers` that takes an integer `n` as input and returns the sum of the first `n` positive even numbers that are not multiples of 4. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_even_numbers(n):
    sum = 0
    count = 0
    num = 2
    
    while count < n:
        if num % 4 != 0:
            sum += num
            count += 1
        num += 2
    
    return sum