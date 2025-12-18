"""
QUESTION:
Create a function named `count_letter` that takes a string and a letter as input and returns the count and positions of the letter in the string. The function should iterate over each character in the string and keep track of the positions of the specified letter. The function should return a tuple containing the count of the letter and a list of its positions. The function should be written in a Pythonic way, using the `enumerate` function to iterate over the characters and their indices in the string.
"""

def count_letter(string, letter):
    count = 0
    positions = []
    for i, char in enumerate(string):
        if char == letter:
            count += 1
            positions.append(i)
    return count, positions