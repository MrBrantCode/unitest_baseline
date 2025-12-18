"""
QUESTION:
Write a function `charcode_sum` that calculates the sum of the ASCII values of all characters in a given string. The function should take a string `word` as input and return its charcode sum. The function should not use any external libraries or built-in sum functions. The ASCII values can be obtained using the `ord` function.
"""

def entance(word):
    sum = 0
    for char in word:
        sum += ord(char)
    return sum