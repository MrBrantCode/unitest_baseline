"""
QUESTION:
Write a function named `longest_substring` that takes two parameters: `s` and `k`, where `s` is a string and `k` is an integer. The function should return the length of the longest substring of `s` that contains exactly `k` unique characters. The solution must have a time complexity of O(n), where n is the length of the input string `s`.
"""

def longest_substring(s, k):
    count = {}
    start = 0
    end = 0
    max_length = 0
    unique_chars = 0

    while end < len(s):
        count[s[end]] = count.get(s[end], 0) + 1
        if count[s[end]] == 1:
            unique_chars += 1

        while unique_chars > k:
            count[s[start]] -= 1
            if count[s[start]] == 0:
                unique_chars -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
        end += 1

    return max_length