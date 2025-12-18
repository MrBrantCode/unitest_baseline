"""
QUESTION:
Design a function named `find_longest_palindrome` to find the longest palindrome inside a given string of lowercase alphabets. The length of the input string will not exceed 10^5 characters. The function should return the starting and ending indices of the longest palindrome substring in the given string. If there are multiple longest palindromes with the same length, the function should return the one with the smallest starting index. The function should achieve this in a time complexity of O(n).
"""

def find_longest_palindrome(string):
    n = len(string)
    start = 0
    max_len = 1
    for i in range(1, n):
        # check for even length palindromes
        left = i - 1
        right = i
        while left >= 0 and right < n and string[left] == string[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
        
        # check for odd length palindromes
        left = i - 1
        right = i + 1
        while left >= 0 and right < n and string[left] == string[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    end = start + max_len - 1
    return start, end