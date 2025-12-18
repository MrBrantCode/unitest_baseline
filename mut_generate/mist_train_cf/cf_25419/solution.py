"""
QUESTION:
Create a function `number_to_word` that takes a two-digit integer `n` as input and returns a string representing the number in words. The input number `n` is between 10 and 99 (inclusive) and does not include numbers that are multiples of 10.
"""

def number_to_word(n):
    tens_words = {
        0: '',
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety',
    }
    ones_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    tens = n // 10
    ones = n % 10

    return tens_words[tens] + ' ' + ones_words[ones]