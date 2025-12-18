"""
QUESTION:
Write a function `is_isomorphic(str1, str2)` that determines if there exists an isomorphic relationship between two given strings. The function should return `True` if the strings are isomorphic and `False` otherwise. An isomorphic relationship exists if the characters in the first string can be replaced to get the second string, with each character in the first string corresponding to exactly one character in the second string, and vice versa. The function should have a time complexity of O(n), where n is the length of the input strings.
"""

def is_isomorphic(str1, str2):
    # If lengths are not same, they cannot be isomorphic.
    if len(str1) != len(str2):
        return False

    # Create a mapping between two strings.
    map_str1_to_str2 = {}
    map_str2_to_str1 = {}

    for i in range(len(str1)):
       if (str1[i] in map_str1_to_str2 and map_str1_to_str2[str1[i]] != str2[i]) or (str2[i] in map_str2_to_str1 and map_str2_to_str1[str2[i]] != str1[i]):
          return False
       map_str1_to_str2[str1[i]] = str2[i]
       map_str2_to_str1[str2[i]] = str1[i]
    return True