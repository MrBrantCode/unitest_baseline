"""
QUESTION:
Write a function named `is_happy` that takes a string `s` as input and returns a boolean value. The function should check if the input string meets the following conditions: 
- It consists only of lowercase alphabets.
- Its length is at least three characters.
- Every sequence of three consecutive characters is unique.
- Each unique character appears at least twice.
- No character appears consecutively.
- The number of characters with the same frequency does not exceed two if the frequency is three or less.
- Each unique character appears an even number of times.
Use a dictionary and a set to check these conditions.
"""

def is_happy(s):
    if len(s) < 3 or not s.isalpha() or not s.islower():
        return False
    
    # count the frequency of each character
    char_dict = {}
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    # check the condition of each unique alphabet having identical counts cannot exceed two
    count_dict = {}
    for char, count in char_dict.items():
        if count not in count_dict:
            count_dict[count] = 1
        else:
            count_dict[count] += 1

    for count, freq in count_dict.items():
        if count <= 3 and freq > 2:
            return False

    # check the condition of consecutive repetitions of the same alphabet
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False

    # check the condition of the uniqueness of every series of three succeeding alphabets
    triplets = {s[i:i+3] for i in range(len(s)-2)}
    if len(triplets) != len(s)-2:
        return False

    # check the condition of each unique character appearing an even number of times
    for char, count in char_dict.items():
        if count % 2 != 0:
            return False

    return True