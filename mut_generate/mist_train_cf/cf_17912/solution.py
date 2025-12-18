"""
QUESTION:
Write a function `compress_string` that compresses a given string by replacing substrings of length 4 or more with the substring and its count. The function should return the compressed string. The input string will only contain characters.
"""

def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        if i < len(string)-1 and string[i] == string[i+1]:
            count += 1
        else:
            if count <= 3:
                compressed_string += string[i] * count
            else:
                compressed_string += string[i] + str(count)
            count = 1
    return compressed_string