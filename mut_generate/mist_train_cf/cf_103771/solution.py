"""
QUESTION:
Create a function called `replace_numbers` that takes two arrays as arguments: `nums` and `symbols`. The function should return a string where each number in `nums` that is divisible by 3 is replaced with the corresponding symbol from `symbols` (assuming the first symbol corresponds to the number 3, the second to 6, and so on). The numbers that are not divisible by 3 should remain unchanged. The output string should be a comma-separated list of the modified numbers and symbols.
"""

def replace_numbers(nums, symbols):
    result = []
    for num in nums:
        if num % 3 == 0:
            result.append(symbols[num // 3 - 1])
        else:
            result.append(str(num))
    return ','.join(result)