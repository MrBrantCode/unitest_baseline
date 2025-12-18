"""
QUESTION:
Create a function named `repeat_characters` that takes a string `s` as an argument. The function should return a string where each character is repeated based on its occurrence count in the string. The repetition pattern should be as follows: the first occurrence of each character is repeated once, the second occurrence is repeated twice, the third occurrence is repeated three times, and so on. However, if the character is a digit, it should be repeated three times regardless of its occurrence count.
"""

def repeat_characters(s):
    updated_string = ""
    counter = {}

    for char in s:
        if char.isdigit():
            repeat = 3
        else:
            repeat = counter.get(char, 0) + 1
            counter[char] = repeat

        updated_string += char * repeat

    return updated_string