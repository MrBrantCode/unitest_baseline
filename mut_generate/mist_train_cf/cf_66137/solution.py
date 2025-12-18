"""
QUESTION:
Create a function named `print_string_n_times` that takes two parameters: `string` and `n`, where `string` is the input string to be printed and `n` is the number of times the string should be printed. The function should use recursion to print the string `n` times. The function should not print anything if `n` is less than or equal to 0.
"""

def print_string_n_times(string, n):
    if n <= 0:
        return
    else:
        print(string)
        print_string_n_times(string, n - 1)