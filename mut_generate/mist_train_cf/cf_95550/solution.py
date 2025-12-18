"""
QUESTION:
Design a function `add_binary_numbers` that takes two binary numbers `binary1` and `binary2` as input, adds them together, and returns the result as a binary string. The function should have a time complexity of O(log n), where n is the length of the longer binary number, and a space complexity of O(1), not using any additional data structures other than the given binary numbers. The function should implement the addition logic from scratch without using built-in functions or operators for binary addition. It should also handle cases where the binary numbers are of different lengths and have leading zeros.
"""

def add_binary_numbers(binary1, binary2):
    ptr1 = int(binary1, 2)
    ptr2 = int(binary2, 2)
    carry = 0
    result = ""

    while ptr1 != 0 or ptr2 != 0:
        sum1 = (ptr1 & 1) + (ptr2 & 1) + carry
        carry = sum1 // 2
        result = str(sum1 % 2) + result
        ptr1 = ptr1 >> 1
        ptr2 = ptr2 >> 1

    if carry:
        result = str(carry) + result

    return result