"""
QUESTION:
Write a function `solve_problem` that takes three parameters: a list of binary strings, a bitwise operation ('&', '|', '^'), and another binary string. The function should remove duplicates from the list, perform the given bitwise operation on each unique binary string with the given binary string, convert the result to decimal, and return the sum of these decimal values. The function should include error handling for invalid inputs.
"""

def solve_problem(input_list, operation, another_binary):
    try:
        unique_binaries = list(set(input_list))  # Remove duplicates
        decimal_sum = 0

        # Perform operation with all unique binary strings
        for binary_str in unique_binaries:
            result_bin = eval(f"int(binary_str, 2) {operation} int(another_binary, 2)")
            decimal_sum += result_bin

        return decimal_sum

    except Exception as e:
        return f"An error occurred: {str(e)}"