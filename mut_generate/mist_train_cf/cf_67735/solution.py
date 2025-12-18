"""
QUESTION:
Develop a function named `count_upper` that takes a string `s` as input and returns the quantity of uppercase vowels situated at even index positions. The function should only consider the English vowels 'A', 'E', 'I', 'O', 'U' as vowels.
"""

def count_upper(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    count = 0
    for index, letter in enumerate(s):
        if index % 2 == 0 and letter in vowels:
            count += 1
    return count