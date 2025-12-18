"""
QUESTION:
Classify all elements in an integer array as even and odd using a bitwise solution, without using the modulus operator or any arithmetic operations. Implement a function called `classify_numbers` that takes an integer array as input and returns two separate lists containing even and odd numbers. The solution must have a time complexity of O(n), where n is the length of the input array, and use constant space.
"""

def classify_numbers(arr):
    even = []
    odd = []
    
    for num in arr:
        if num & 1 == 0:  # Check if LSB is 0
            even.append(num)
        else:
            odd.append(num)
    
    return even, odd