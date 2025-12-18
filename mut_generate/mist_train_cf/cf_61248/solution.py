"""
QUESTION:
Create a function called `alternate_string` that takes two strings `str1` and `str2` as input and returns a new string where characters from `str1` and `str2` are alternated. If one string is longer than the other, append the remaining characters from the longer string at the end.
"""

def alternate_string(str1, str2):
    # find the shorter length of the two strings
    min_len = min(len(str1), len(str2))

    # iterate up to this shorter length and 
    # concatenate a character from each string in turn
    alternated_string = ''.join([str1[i] + str2[i] for i in range(min_len)])

    # if one string is longer, append the rest of this string
    if len(str1) > len(str2):
        alternated_string += str1[min_len:]
    elif len(str2) > len(str1):
        alternated_string += str2[min_len:]

    return alternated_string