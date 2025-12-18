"""
QUESTION:
Write a function named `replace_nums_with_symbols` that takes two arrays, `nums` and `symbols`, as arguments. The function should return a string where each number in `nums` that is divisible by 3 but not by 2 is replaced with the corresponding symbol from the `symbols` array (reversed before replacement). Numbers not meeting this condition should be left unchanged. The function should return the modified numbers and symbols as a comma-separated string.
"""

def replace_nums_with_symbols(nums, symbols):
    symbols = symbols[::-1]
    output = []
    for num in nums:
        if num % 3 == 0 and num % 2 != 0:
            output.append(symbols.pop())
        else:
            output.append(str(num))
    return ",".join(output)