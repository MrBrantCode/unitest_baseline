"""
QUESTION:
Write a function named `is_narcissistic_number` that takes an integer `num` as input and returns a boolean value indicating whether the number is a Narcissistic number or not. A Narcissistic number is defined as an n-digit number that is equal to the sum of its own digits each raised to the power of n. The input integer will be within the range of 1 to 10^9. The solution should have a time complexity of O(log(n)) and a space complexity of O(1).
"""

def is_narcissistic_number(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** n
    return sum == num