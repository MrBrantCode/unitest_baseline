"""
QUESTION:
Write a function `compress_string` that takes a string as input and returns a compressed string. The compressed string is formed by replacing substrings of length 4 or more with the character and its count. If the length of the substring is 3 or less, append the character that many times.
"""

def compress_string(string):
    compressed_string = ""
    count = 1
    for i in range(len(string)):
        # If the current character is the same as the next character
        if i < len(string)-1 and string[i] == string[i+1]:
            count += 1
        else:
            # If the count is less than or equal to 3, append the character count times
            if count <= 3:
                compressed_string += string[i] * count
            else:
                # If the count is greater than 3, append the character and its count
                compressed_string += string[i] + str(count)
            count = 1
    return compressed_string