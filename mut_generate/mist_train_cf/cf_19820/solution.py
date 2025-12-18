"""
QUESTION:
Create a function called `check_order_and_spacing` that takes two strings as input, `str1` and `str2`. The function should return `True` if the characters in `str1` appear in the same order as in `str2`, with each character in `str2` followed by at least one space before the next character, and `False` otherwise. The function should have a time complexity of O(n+m), where n and m are the lengths of `str1` and `str2` respectively.
"""

def check_order_and_spacing(str1, str2):
    char_list1 = list(str1)
    char_list2 = list(str2)
    
    pointer1 = 0
    pointer2 = 0
    
    while pointer1 < len(char_list1) and pointer2 < len(char_list2):
        if char_list1[pointer1] == char_list2[pointer2]:
            pointer1 += 1
            pointer2 += 1
        elif char_list2[pointer2] == ' ':
            pointer2 += 1
        else:
            return False
    
    if pointer1 == len(char_list1) and char_list2[pointer2:].count(' ') != len(char_list2[pointer2:]):
        return False
    
    return pointer1 == len(char_list1) and pointer2 == len(char_list2)