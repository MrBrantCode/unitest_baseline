"""
QUESTION:
Write a function `count_words_in_lines` that takes a poem as a string input and returns a list of word counts for each line in the poem. The input string is expected to contain multiple lines separated by newline characters, and words within each line are separated by spaces. The function should split the input string into lines, then split each line into words and count the number of words in each line.
"""

def count_words_in_lines(poem):
    lines = poem.split("\n")
    return [len(line.split()) for line in lines if line] 