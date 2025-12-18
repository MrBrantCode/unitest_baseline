"""
QUESTION:
Given a string `s`, return the maximum number of occurrences of any substring under the following rules: 
- The number of unique characters in the substring must be less than or equal to `maxLetters`.
- The substring size must be between `minSize` and `maxSize` inclusive.
- The substring must not contain any repeating sequence of characters.
 
Restrictions: 
- `1 <= s.length <= 10^5`
- `1 <= maxLetters <= 26`
- `1 <= minSize <= maxSize <= min(26, s.length)`
- `s` only contains lowercase English letters.

Required function: `maxFreq(s, maxLetters, minSize, maxSize)`.
"""

from collections import defaultdict

def maxFreq(s, maxLetters, minSize, maxSize):
    window_counts = defaultdict(int)
    total_counts = defaultdict(int)
    res = 0
    for i in range(len(s)):
        window_counts[s[i]] += 1
        if i >= minSize:
            window_counts[s[i-minSize]] -= 1
            if window_counts[s[i-minSize]] == 0:
                del window_counts[s[i-minSize]]
        if i >= minSize - 1 and len(window_counts) <= maxLetters:
            total_counts[s[i-minSize+1:i+1]] += 1
            res = max(res, total_counts[s[i-minSize+1:i+1]])
    return res