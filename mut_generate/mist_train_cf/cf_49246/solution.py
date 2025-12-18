"""
QUESTION:
Write a function named `multiply` that takes a dictionary as input where keys represent indices and values are integers. The function should return the product of the values that meet the following conditions: 
- The key is even and the corresponding value is odd and divisible by 3.
- The value is divisible by 5.

The input dictionary is non-empty.
"""

def multiply(dictionary):
    product = 1
    for key, value in dictionary.items():
        if key % 2 == 0 and value % 3 == 0 and value % 2 != 0:
            product *= value
        elif value % 5 == 0:
            product *= value            
    return product