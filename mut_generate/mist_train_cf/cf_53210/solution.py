"""
QUESTION:
Create a function `remove_repeats_and_count` that takes a string `s` as input. The function should ignore spaces and case sensitivity, eliminate repeated characters from the string, and count the number of occurrences of each character in the original string. The function should return a string without repeat characters and a dictionary with the count of each character. The output string should maintain the original order of characters.
"""

def remove_repeats_and_count(s):
    s = s.replace(" ", "").lower()
    A = {}
    no_repeats = []    
    for i in s:
        if i in A:
            A[i] += 1
        elif i not in no_repeats:
            no_repeats.append(i)
            A[i] = 1
    return ''.join(no_repeats), A