"""
QUESTION:
Write a function `decimal_to_binary(n)` that converts a given decimal number `n` to its binary representation without using any built-in functions or libraries for number conversion. The function should have a time complexity of O(log n).
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