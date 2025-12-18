"""
QUESTION:
Implement a function `find_3rd_o` that finds the location of the 3rd occurrence of the letter 'o' in a given string. The function should use a recursive algorithm and must not use any string manipulation functions or methods. The function should return the index of the 3rd 'o' if found, and -1 otherwise. The index is 0-based, but the returned index should be 1-based (i.e., the first character is at position 1).
"""

def find_3rd_o(string, index=0, count=0):
    if count == 3:
        return index  # Return the index of the last 'o'
    if index >= len(string):
        return -1  # Return -1 if 'o' is not found three times

    if string[index] == 'o':
        count += 1

    return find_3rd_o(string, index + 1, count)