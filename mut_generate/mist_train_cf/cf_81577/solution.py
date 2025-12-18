"""
QUESTION:
Write a function `extract_substrings(input_str, key_letter)` that takes a character sequence `input_str` of length N and a specific key letter `key_letter` K as input, and returns all palindrome substrings within the sequence that begin and end with the key letter K.
"""

def extract_substrings(input_str, key_letter):
    n = len(input_str)
    result = []
    for i in range(n):
        for j in range(i+1, n+1):
            temp = input_str[i:j]
            if temp[0] == temp[-1] == key_letter and temp == temp[::-1]:
                result.append(temp)
    return result