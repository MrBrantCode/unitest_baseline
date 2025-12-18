"""
QUESTION:
Write a function named `find_divisible_by_five` that takes a list of binary numbers as input and returns a new list containing only the binary numbers that are divisible by 5. The function should handle erroneous entries in the list, including non-binary numbers and non-string inputs.
"""

def find_divisible_by_five(binary_list):
    result = []
    for binary in binary_list:
        if isinstance(binary, str):
            try:
                decimal = int(binary, 2)
                if decimal % 5 == 0:
                    result.append(binary)
            except ValueError:
                print(f"Invalid binary number: {binary}")
                continue
    return result