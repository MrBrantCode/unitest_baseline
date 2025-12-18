"""
QUESTION:
Create a function `are_isomorphic(string1, string2)` that takes two strings as input and returns a boolean indicating whether the two strings are isomorphic. Two strings are isomorphic if the characters in one string can be replaced to get the other string, and this replacement should be one-to-one, i.e., a character in the first string can be replaced by only one character in the second string, and vice versa. The function should not use any built-in functions for isomorphism check and should handle edge cases.
"""

def are_isomorphic(string1, string2):
    if len(string1) != len(string2):  
        return False
    dict_s = dict()
    for index in range(len(string1)):
        if string1[index] in dict_s:  
            if dict_s[string1[index]] != string2[index]:  
                return False  
        elif string2[index] in dict_s.values():  
            return False  
        else:
            dict_s[string1[index]] = string2[index]  
    return True  