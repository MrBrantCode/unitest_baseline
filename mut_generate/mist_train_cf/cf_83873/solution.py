"""
QUESTION:
Write a function "is_happy" that takes a string "s" and returns True if it fits the 'happy' criteria, False otherwise. The 'happy' criteria are: the string length should be at least 3, all sequences of three successive letters should be unique, and each character should appear at least twice but not in consecutive positions.
"""

def is_happy(s):
    if len(s) < 3:
        return False

    # Dict for tracking frequencies and last index of characters
    freq = {}
    # Set for tracking unique sequences of 3 letters
    seen = set()

    for i, char in enumerate(s):
        if char in freq:
            if i - freq[char][1] == 1 or freq[char][0] < 2:
                freq[char][0] += 1
                freq[char][1] = i
            else:
                return False
        else:
            freq[char] = [1, i]

        if i >= 2:
            seq = s[i-2:i+1]
            if seq in seen:
                return False
            seen.add(seq)

    for v in freq.values():
        if v[0] < 2:
            return False

    return True