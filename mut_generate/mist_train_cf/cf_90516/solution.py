"""
QUESTION:
Write a function 'combineStrings' that takes two strings and a delimiter as input. The function should return the combined string with the delimiter between the two strings. If one or both of the input strings are empty, the function should still return the combined string with the delimiter. The delimiter can be of any length. The time complexity of the function should be O(n), where n is the total length of the input strings.
"""

def combineStrings(string1, string2, delimiter):
    if not string1 and not string2:  
        return delimiter
    elif not string1:  
        return delimiter + string2
    elif not string2:  
        return string1 + delimiter
    else:  
        return string1 + delimiter + string2