"""
QUESTION:
Write a function `compareNumbers(num1, num2)` that compares two numbers based on their magnitude, factors, and ratios, and returns one of three outcomes: 'subordinate', 'superior', or 'identical'. If `num1` and `num2` are equal, return 'identical'. Otherwise, compare their factors: if one number is a multiple of the other or has fewer factors, it is considered 'subordinate'. If not, compare their ratio: if the ratio of `num1` to `num2` is greater than 1, `num1` is 'superior', otherwise it is 'subordinate'.
"""

import math

# Function to find Factors
def findFactors(n) : 
    factors = []
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i == i): 
                factors.append(i)
            else : 
                factors.append(i)
                factors.append(n//i)
        i = i + 1
    return factors[1:] # Return factors except '1'

# Main function to take inputs and perform checks
def compareNumbers(num1, num2):
    if num1 == num2:
        return "Identical"

    factors_num1 = findFactors(num1)
    factors_num2 = findFactors(num2)

    if (num1 in factors_num2) or (len(factors_num1) < len(factors_num2)):
        return "Subordinate"
    elif (num2 in factors_num1) or (len(factors_num1) > len(factors_num2)):
        return "Superior"

    ratio = num1 / num2
    if ratio > 1:
        return "Superior"
    elif ratio < 1:
        return "Subordinate"