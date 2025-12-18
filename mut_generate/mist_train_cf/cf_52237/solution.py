"""
QUESTION:
Create a function `decimal_to_binary(n)` that takes a non-negative integer `n` and returns a tuple containing the binary representation of `n` as a string and the count of '1' bits in the binary representation. The function must use a custom recursive algorithm and not utilize built-in binary conversion methods or the `bin()` function. Implement proper error handling to return error messages for non-integer and negative inputs.
"""

def decimal_to_binary(n):
    if type(n) is not int:
        return "Error: Input should be an integer"
    if n < 0:
        return "Error: Input should be a non-negative integer"
        
    def binary_helper(n):
        if n == 0:
            return '0', 0
        elif n == 1:
            return '1', 1
        else:
            bits, count = binary_helper(n // 2)
            bit = n % 2
            return bits + str(bit), count + bit
    return binary_helper(n)