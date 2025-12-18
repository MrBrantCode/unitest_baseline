"""
QUESTION:
Write a function that takes a string as input and reverse only the vowels of a string.


Example 1:
Given s = "hello", return "holle".



Example 2:
Given s = "leetcode", return "leotcede".



Note:
The vowels does not include the letter "y".
"""

def reverse_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    char_list = list(s)
    (first, last) = (0, len(char_list) - 1)
    
    while first < last:
        while first < last and char_list[first] not in vowels:
            first += 1
        while first < last and char_list[last] not in vowels:
            last -= 1
        if first >= last:
            break
        (char_list[first], char_list[last]) = (char_list[last], char_list[first])
        first += 1
        last -= 1
    
    return ''.join(char_list)