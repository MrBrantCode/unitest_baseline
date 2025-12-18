"""
QUESTION:
Create a function `sort_and_reverse_strings` that takes a 2D list of strings as input. The function should sort the strings in descending order of length and reverse the order of the characters for each string. The function should be able to handle strings with special characters and white spaces. The input table is represented as a 2D list where each inner list represents a string and each element in the inner list represents a character of the string.
"""

def sort_and_reverse_strings(table):
    # Sort the strings in descending order of length
    table.sort(key=len, reverse=True)
    # Reverse the order of the characters for each string
    for i in range(len(table)):
        table[i] = table[i][::-1]
    return table