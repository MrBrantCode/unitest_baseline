"""
QUESTION:
Write a function `get_number_word(num)` that takes an integer as input and returns its word representation as a string. The function should handle integers from 1 to 999,999.
"""

def get_number_word(num):
    num_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    if num in num_dict:
        return num_dict[num]
    elif num < 100:
        return num_dict[num - num % 10] + ' ' + num_dict[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            return num_dict[num // 100] + ' hundred'
        else:
            return num_dict[num // 100] + ' hundred and ' + get_number_word(num % 100)
    elif num < 1000000:
        if num % 1000 == 0:
            return get_number_word(num // 1000) + ' thousand'
        else:
            return get_number_word(num // 1000) + ' thousand, ' + get_number_word(num % 1000)
    return None