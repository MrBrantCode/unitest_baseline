"""
QUESTION:
Write a function named `compress_string` that takes a string as input and returns a compressed version of the string. The compressed string should contain tuples of characters and their consecutive occurrence counts, without using any built-in functions or methods for string manipulation or counting.
"""

def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        if i != len(string) - 1 and string[i] == string[i + 1]:
            count += 1
        else:
            compressed_string += "(" + string[i] + "," + str(count) + ")"
            count = 1
    return compressed_string