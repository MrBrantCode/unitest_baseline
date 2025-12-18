"""
QUESTION:
Write a function `classify_elements` that takes an array of integers as input and returns two lists of integers, one containing all even numbers and the other containing all odd numbers. The function should use a bitwise solution to determine the parity of each element and should not use any arithmetic operations, modulus operator (%), built-in functions, or libraries for bitwise operations. The time complexity of the function should be O(n), where n is the length of the input array, and the space complexity should be O(n).
"""

def classify_elements(arr):
    even = []
    odd = []
    for num in arr:
        if num & 1 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd