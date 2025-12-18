"""
QUESTION:
Implement a function called `advanced_histogram` that takes a string of characters (including uppercase & lowercase letters, numbers, and punctuation marks) as input. The function should return a dictionary displaying the frequency of each character, considering uppercase and lowercase letters equivalent and represented in lowercase. If multiple characters show the same highest frequency, return all of them. The function should ignore spaces in the input string.
"""

def advanced_histogram(s):
    count = {}
    for char in s:
        if char != ' ':
            if char.lower() in count:
                count[char.lower()] += 1
            else:
                count[char.lower()] = 1
    max_freq = max(count.values(), default=0)
    return {k: v for k, v in count.items() if v == max_freq}