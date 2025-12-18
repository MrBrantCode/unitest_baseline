"""
QUESTION:
Write a function named `longest_substring` that takes a string `s`, an integer `k`, and an integer `m` as input, and returns the length of the longest substring of `s` such that the frequency of each character in this substring is greater than or equal to `k` and the number of unique characters in the substring is exactly `m`. 

The input string `s` consists of only lowercase English letters and its length is between 1 and 10^4. The value of `k` is between 1 and 10^5, and the value of `m` is between 1 and 26.
"""

def longest_substring(s, k, m):
    max_length = 0
    for unique in range(1, m + 1):
        start = 0
        count = [0]*26
        freq_at_least_k = 0
        unique_char_counter = 0
        for end in range(len(s)):
            if count[ord(s[end]) - ord('a')] == 0:
                unique_char_counter += 1
            count[ord(s[end]) - ord('a')] += 1
            if count[ord(s[end]) - ord('a')] == k:
                freq_at_least_k += 1
                
            while unique_char_counter > unique:
                if count[ord(s[start]) - ord('a')] == k:
                    freq_at_least_k -= 1
                count[ord(s[start]) - ord('a')] -= 1
                if count[ord(s[start]) - ord('a')] == 0:
                    unique_char_counter -= 1
                start += 1
                
            if unique_char_counter == freq_at_least_k == unique and end - start + 1 > max_length:
                max_length = end - start + 1
    return max_length