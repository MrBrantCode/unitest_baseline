"""
QUESTION:
Create a function `reverse_and_count_vowels` that takes a string as input and returns a tuple containing the reversed string and the count of vowels in the reversed string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_and_count_vowels(s):
    reversed_string = ""
    vowel_count = 0
    vowels = set("aeiouAEIOU")
         
    for i in range(len(s) - 1, -1, -1):
        char = s[i]
        reversed_string += char
        if char in vowels:
            vowel_count += 1
    return reversed_string, vowel_count