"""
QUESTION:
Implement a function `get_decimal_sum(decimal_digit_words)` that takes a list of strings as input, where each string represents a decimal digit word in the American number system. The function should convert each word to its corresponding decimal digit and return their sum as a float. If the input list contains any invalid decimal word, the function should return 0. The American number system uses the following decimal digit words: zero, one, two, three, four, five, six, seven, eight, nine.
"""

def get_decimal_sum(decimal_digit_words):
    decimal_words = {'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}
    american_number_system = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    decimal_number_sum = 0
    for dec_word in decimal_digit_words:
        if dec_word not in decimal_words:
            return 0
        else:
            decimal_number_sum += american_number_system[dec_word]

    return float(decimal_number_sum)