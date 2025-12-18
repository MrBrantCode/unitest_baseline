"""
QUESTION:
Create a function `reverse_words` that takes a string of alphanumeric characters and spaces as input, reverses each word in the string, and returns the result as a new string with the same spacing and word order. The function should achieve this in O(n) time complexity, where n is the length of the string, and use constant space complexity, excluding the space required for the output string.
"""

def reverse_words(s):
    result = []
    word = []
    for char in s:
        if char == " ":
            result.append("".join(word[::-1]))
            word = []
        else:
            word.append(char)
    result.append("".join(word[::-1]))
    return " ".join(result)