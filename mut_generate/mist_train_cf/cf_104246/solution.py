"""
QUESTION:
Create a function `count_chars` that takes a string as input and returns a dictionary where the keys are characters from the string and the values are the number of occurrences of each character. Create another function `print_char_count` that takes the dictionary returned by `count_chars` as input and prints the characters and their occurrence counts in descending order of occurrence count. 

The `count_chars` function should return a dictionary and the `print_char_count` function should not return any value. The input string and the dictionary should be of type `str` and `dict` respectively.
"""

def count_chars(input_str: str) -> dict:
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_char_count(char_count: dict) -> None:
    sorted_chars = sorted(char_count, key=char_count.get, reverse=True)
    for char in sorted_chars:
        print(char, char_count[char])