"""
QUESTION:
Write a function `classify_elements(arr)` that takes an integer array `arr` as input and returns two lists, one for even numbers and one for odd numbers. The function should use a bitwise solution to classify the numbers, without using the modulus operator (%) or any arithmetic operations. The time complexity of the solution should be O(n), where n is the length of the input array, and the solution should use only constant space, excluding the space needed for the output.
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