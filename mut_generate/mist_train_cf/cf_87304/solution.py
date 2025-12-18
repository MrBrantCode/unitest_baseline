"""
QUESTION:
Write a function `decimal_to_binary(n)` that takes a positive decimal integer `n` as input and returns its binary representation as a string. The solution should have a time complexity of O(log n), where n is the given decimal number. The binary representation should be calculated without using any built-in functions or libraries for number conversion.
"""

def decimal_to_binary(n):
    binary = ""
    stack = []
    
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    
    while stack:
        binary += str(stack.pop())
    
    return binary