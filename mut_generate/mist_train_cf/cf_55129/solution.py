"""
QUESTION:
Write a function named `character_search` that takes two parameters: an input string `string` and a character `char`. The function should determine if `char` is present in `string`, and if so, return its frequency and the index of its first occurrence. If `char` is not present in `string`, the function should return a custom message indicating its absence. The function should be efficient in terms of time complexity, and the index position should start from zero.
"""

def character_search(string, char):
    if string.count(char) == 0:
        return f"The character '{char}' is not present in the string."
    
    freq = string.count(char)
    first = string.find(char)

    return (
        f"The character '{char}' is present.\n"
        f"Frequency: {freq} times.\n"
        f"First Occurrence: {first}th position."
    )