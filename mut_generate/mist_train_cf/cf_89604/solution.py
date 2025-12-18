"""
QUESTION:
Implement a function called `bitwise_and_count` that takes two integers `num1` and `num2` as input and returns the number of bits that are set to 1 in their bitwise AND result. You are not allowed to use any built-in functions or libraries for this task.
"""

def bitwise_and_count(num1, num2):
    bitwise_and = num1 & num2  
    count = 0
    while bitwise_and > 0:
        if bitwise_and & 1:  
            count += 1
        bitwise_and = bitwise_and >> 1  
    return count