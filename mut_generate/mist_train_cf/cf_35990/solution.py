"""
QUESTION:
Write a function `countSubstrings` that takes a string `s` of lowercase English letters as input and returns the total count of all possible substrings of `s` that contain all three letters 'a', 'b', and 'c' at least once. The count of each letter in the substring does not matter.
"""

def countSubstrings(s: str) -> int:
    left, right = 0, 0
    subStringCount = 0
    counter = {c: 0 for c in 'abc'}
    
    while right < len(s):
        counter[s[right]] += 1
        while all(counter.values()):
            counter[s[left]] -= 1
            left += 1
            subStringCount += 1  # Increment the count for each valid substring found
        right += 1
    
    return subStringCount