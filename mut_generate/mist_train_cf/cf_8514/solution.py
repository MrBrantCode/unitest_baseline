"""
QUESTION:
Write a function named `switch_string` that takes a string `str` as input. The function should split the string into two parts at an index determined by the string's length. If the length is odd, the index should be the middle character. If the length is even, the index should be the second character from the middle. The function should then return the resulting string with the order of the two parts switched.
"""

def switch_string(str):
    length = len(str)
    if length % 2 == 1:
        index = length // 2
    else:
        index = length // 2 + 1
    
    part1 = str[:index]
    part2 = str[index:]
    
    return part2 + part1