"""
QUESTION:
Write a function `numberOfSubstrings(s)` that takes a string `s` of length at least 3 and at most 5 x 10^4, composed solely of the characters 'a', 'b', and 'c', and returns the number of substrings that include at least one instance of each of these characters.
"""

def numberOfSubstrings(s):
    count = [0]*3
    left, right = 0, 0
    res = 0
    while right < len(s):
        count[ord(s[right]) - ord('a')] += 1
        while all(x>0 for x in count):
            count[ord(s[left]) - ord('a')] -= 1
            left += 1
        res += left
        right += 1
    return res