"""
QUESTION:
Write a function `sort_numbers(numbers: str) -> str` that takes a space-separated string of numerals written in words, ranging from 'zero' to 'nine', and returns a string with the numbers arranged in ascending order. The function should be case-sensitive and only accept the exact word spellings for the numbers 'zero' to 'nine'.
"""

def sort_numbers(numbers: str) -> str:
    num_dic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    words = numbers.split()
    sorted_words = sorted(words, key=lambda x: num_dic[x])
    return ' '.join(sorted_words)