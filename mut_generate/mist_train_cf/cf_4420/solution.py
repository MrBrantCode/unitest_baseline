"""
QUESTION:
Add two binary numbers with the following constraints:
The function should be named add_binary_numbers and it should take three parameters: two binary numbers and the base of the numbers.
- The time complexity should be O(log n), where n is the length of the longer binary number.
- The space complexity should be O(1), i.e., the algorithm should not use any additional data structures other than the given binary numbers.
- The function should handle cases where the binary numbers are of different lengths and the binary numbers can have leading zeros. 
- The function should also handle cases where the binary numbers are represented as strings.
"""

def add_binary_numbers(num1, num2, base):
    result = ''
    carry = 0
    
    i, j = len(num1) - 1, len(num2) - 1
    
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(num1[i], base)
            i -= 1
        if j >= 0:
            carry += int(num2[j], base)
            j -= 1
        
        result = str(carry % base) + result
        carry //= base
    
    return result