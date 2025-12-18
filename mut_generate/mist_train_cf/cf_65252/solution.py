"""
QUESTION:
Given a string `s` and an integer `k`, write a function `maxVowels` to find the maximum count of vowel letters present in any substring of `s` that has a length equivalent to `k`. Vowel letters are 'a', 'e', 'i', 'o', and 'u'. The string `s` is composed of lowercase English letters and has a length between 1 and 10^5. The integer `k` is between 1 and the length of `s`.
"""

def maxVowels(s: str, k: int) -> int:
    vowels = set('aeiou')  
    cnt = sum(1 for c in s[:k] if c in vowels)  
    max_cnt = cnt  

    for i in range(k, len(s)):
        cnt -= s[i - k] in vowels
        cnt += s[i] in vowels
        max_cnt = max(max_cnt, cnt)

    return max_cnt