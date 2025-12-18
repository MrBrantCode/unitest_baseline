"""
QUESTION:
Write a function `common_alphabets(str1, str2, case_insensitive=True)` that takes two strings and an optional boolean parameter `case_insensitive` as input, and returns a dictionary where the keys are the common alphabetical characters between the two strings and the values are the minimum counts of these characters in both strings. The function should ignore non-alphabetic characters and consider or ignore the case of the characters based on the `case_insensitive` parameter.
"""

def common_alphabets(str1, str2, case_insensitive=True):
    # Filter out non-alphabetic characters and adjust case
    str1 = ''.join(filter(str.isalpha, str1))
    str2 = ''.join(filter(str.isalpha, str2))
    
    if case_insensitive: 
        str1 = str1.lower()
        str2 = str2.lower()

    common_char = set(str1).intersection(set(str2))
    common_char_dict = {}

    for char in common_char:
        common_char_dict[char] = min(str1.count(char), str2.count(char))
        
    return common_char_dict