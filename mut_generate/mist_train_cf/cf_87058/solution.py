"""
QUESTION:
Write a function `find_3rd_o` that finds the index of the 3rd occurrence of the letter 'o' in a given string using a recursive algorithm without using any string manipulation functions or methods. The function should return -1 if 'o' is not found three times.
"""

def find_3rd_o(string, index=0, count=0):
    if count == 3:
        return index - 1  
    if index >= len(string):
        return -1  

    if string[index] == 'o':
        count += 1

    return find_3rd_o(string, index + 1, count)