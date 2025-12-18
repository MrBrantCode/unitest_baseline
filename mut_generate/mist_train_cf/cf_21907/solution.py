"""
QUESTION:
Write a function `replace_numbers(nums, symbols)` that takes two arrays as arguments: `nums` containing numbers and `symbols` containing symbols. The function should return a string where each number in `nums` is replaced with its associated symbol from `symbols` if the number is divisible by 3. If a number is divisible by both 3 and 5, it should be replaced with the concatenation of its associated symbols. If a number is not divisible by 3, it should remain unchanged. The symbols should be assigned to numbers based on their index in the `symbols` array, starting from the last symbol. If all symbols have been used, the function should reset the symbol index to the last symbol in the `symbols` array.
"""

def replace_numbers(nums, symbols):
    symbol_index = len(symbols) - 1  # start from the last symbol
    output = ""
    for num in nums:
        if num % 3 == 0:
            if num % 5 == 0:
                output += symbols[symbol_index] + symbols[symbol_index - 1]  # concatenate symbols if divisible by both 3 and 5
            else:
                output += symbols[symbol_index]  # replace with symbol if divisible by 3 only
        else:
            output += str(num)  # keep the number unchanged if not divisible by 3
        output += ","
        symbol_index -= 1
        if symbol_index < 0:
            symbol_index = len(symbols) - 1  # reset symbol index if all symbols have been used
    return output[:-1]  # remove the extra comma at the end