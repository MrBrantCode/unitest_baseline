"""
QUESTION:
Implement a function called `is_happy_complex(s)` that checks if a given string `s` is 'happy' or not. A 'happy' string needs to meet the following conditions:

- Have at least three characters.
- Each set of three consecutive letters should be unique.
- Each unique letter appears at least twice.
- No letter repeats consecutively.

Additionally, maintain a dictionary to track the frequency of each character throughout the process.
"""

def is_happy_complex(s):
    if len(s) < 3:
        return False

    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            
    for key in count:
        if count[key] < 2 or (s.find(key*2) != -1):
            return False

    triset = set()
    for i in range(len(s)-2):
        triplet = s[i:i+3]
        if triplet in triset:
            return False
        triset.add(triplet)

    return True