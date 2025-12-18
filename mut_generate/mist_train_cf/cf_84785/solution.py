"""
QUESTION:
Write a function `string_analysis` that takes two input strings `string1` and `string2` and returns a tuple containing three values. The function should determine if the input strings are anagrams of each other, calculate the total number of unique characters in both strings combined, and find the longest common substring of both strings. The function should return a tuple in the format `(is_anagram, unique_chars, longest_common_substring)`. The function should work with any two input strings.
"""

from typing import Tuple

def string_analysis(string1: str, string2: str) -> Tuple[bool, int, str]:
    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)

    # Determining whether they are anagram
    is_anagram = sorted_str1 == sorted_str2

    # Calculating number of unique characters
    unique_chars = len(set(string1 + string2))

    length = 0
    start = 0
    #Finding the longest common substring
    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i and j and string1[i-1]==string2[j - 1]:
                if dp[i - 1][j - 1] + 1 > length:
                    length = dp[i - 1][j - 1] + 1
                    start = i - 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
    longest_common_substring = string1[start-length+1 : start+1]

    return is_anagram, unique_chars, longest_common_substring