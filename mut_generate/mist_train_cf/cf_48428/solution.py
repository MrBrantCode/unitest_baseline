"""
QUESTION:
Write a function named `count_options` that takes a string `s` as input and returns the count of uppercase vowels at even indices and lowercase vowels at odd indices in the string. The function should consider spaces as legal characters and treat the index 0 as an even index.
"""

def count_options(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in vowels[5:]:
            count += 1
        elif i % 2 != 0 and s[i] in vowels[:5]:
            count += 1
    return count