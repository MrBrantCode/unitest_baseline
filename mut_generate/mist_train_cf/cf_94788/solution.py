"""
QUESTION:
Implement a function named `get_alphabetical_order` that takes two strings as input and returns an integer representing their alphabetical order. The function should determine the order by comparing characters based on their ASCII values without using built-in string comparison functions or methods. The input strings contain only lowercase letters and are not empty. The function should return a negative integer if the first string comes before the second, zero if they are equal, and a positive integer if the first string comes after the second.
"""

def get_alphabetical_order(str1, str2):
    i = 0
    while i < len(str1) and i < len(str2):
        if ord(str1[i]) < ord(str2[i]):
            return -1
        elif ord(str1[i]) > ord(str2[i]):
            return 1
        i += 1
    
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0