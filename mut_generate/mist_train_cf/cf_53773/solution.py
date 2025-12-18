"""
QUESTION:
Write a function 'find_gcd' that takes a list of integers as input and returns their greatest common divisor (GCD). The function should handle cases where the input list contains 0 or negative integers, returning a meaningful error message in these situations.
"""

def find_gcd(num_list):
    if 0 in num_list:
        return "Error: The list contains zero."
    if any(i < 0 for i in num_list):
        return "Error: The list contains negative integers."

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    result = num_list[0]
    for num in num_list[1:]:
        result = gcd(result, num)
    return result