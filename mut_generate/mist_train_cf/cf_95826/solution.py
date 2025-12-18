"""
QUESTION:
Create a function `check_order_and_spacing` that takes two strings as input. The function should return `True` if the characters in the first string appear in the same order as in the second string, with the additional constraint that each character in the second string is followed by at least one space character before the next character. The function should return `False` otherwise. The time complexity of the function should be O(n+m), where n and m are the lengths of the two strings respectively.
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