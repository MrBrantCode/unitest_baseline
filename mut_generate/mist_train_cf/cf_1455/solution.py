"""
QUESTION:
Write a function `addWithoutPlus(num1, num2)` that adds two integers without using the '+' operator. The function should work with both positive and negative integers and have a time complexity of O(1) is not possible with this algorithm so at least make sure the time complexity is not worse than O(log n) due to the while loop.
"""

def addWithoutPlus(num1, num2):
    while num2 != 0:
        sum = num1 ^ num2
        carry = (num1 & num2) << 1

        num1 = sum
        num2 = carry

    return num1