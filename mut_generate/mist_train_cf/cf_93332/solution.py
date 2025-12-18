"""
QUESTION:
Write a function `classify_parity` that takes an array of integers as input and returns two lists, one containing even numbers and the other containing odd numbers. You cannot use the modulus operator (%) to determine the parity of each number.
"""

def classify_parity(arr):
    even_numbers = []
    odd_numbers = []
    
    for num in arr:
        if num & 1 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    return even_numbers, odd_numbers