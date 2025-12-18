"""
QUESTION:
Write a function called `compare_strings` that takes two strings as input and returns the index position where the strings first differ if they are not equal. If the strings are equal, return a message indicating they are equal.
"""

def compare_strings(str1, str2):
    if str1 == str2:
        return "The strings are equal."
    else:
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return f"The strings differ at index position {i}."
        return "One string is a prefix of the other."