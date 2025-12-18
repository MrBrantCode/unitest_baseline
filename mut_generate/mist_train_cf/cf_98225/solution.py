"""
QUESTION:
Generate a list of all narcissistic numbers within the range of 100 to 500. The function should be named `is_narcissistic` and should be able to check if a given number is a narcissistic number. A narcissistic number is a non-negative integer of N digits where the sum of the Nth power of each digit is equal to the number itself. The solution should involve at least 3 consecutive logical steps.
"""

def is_narcissistic(num):
    # convert the number to a string and get the length
    num_str = str(num)
    n = len(num_str)
    # calculate the sum of the Nth power of each digit
    sum_digits = sum(int(digit)**n for digit in num_str)
    # return True if the sum is equal to the number
    return num == sum_digits