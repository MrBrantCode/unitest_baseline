"""
QUESTION:
Implement a function `add_arrays(arr1, arr2)` that takes two arrays representing non-negative integers as input and returns their sum as an array. The function should use a stack data structure, support decimal numbers, and have a time complexity of O(n), where n is the number of digits in the larger of the two numbers. The space complexity should be O(1), excluding the space needed for the output.
"""

def add_arrays(arr1, arr2):
    # Reverse both arrays to start from the least significant digit
    arr1 = arr1[::-1]
    arr2 = arr2[::-1]

    # Initialize a stack to store the digits of the sum
    stack = []

    # Initialize carry to 0
    carry = 0

    # Get the length of the larger array
    length = max(len(arr1), len(arr2))

    # Iterate through the digits of both arrays
    for i in range(length):
        # Get the digits at the current position in both arrays
        digit1 = arr1[i] if i < len(arr1) else 0
        digit2 = arr2[i] if i < len(arr2) else 0

        # Add the digits and the carry
        total = digit1 + digit2 + carry

        # Update the carry
        carry = total // 10

        # Add the least significant digit to the stack
        stack.append(total % 10)

    # If there is still a carry, add it to the stack
    if carry > 0:
        stack.append(carry)

    # Reverse the stack to get the sum in the correct order
    stack = stack[::-1]

    # Convert the stack to a list and return it
    return list(stack)