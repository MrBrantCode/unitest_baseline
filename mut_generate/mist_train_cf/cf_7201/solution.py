"""
QUESTION:
Write a function called `largest_palindrome_substring` that takes an array of integers as input and returns the length of the largest palindrome substring within the array. The function should return the length of the first longest palindrome found if there are multiple palindromes with the same maximum length. The palindrome substring can be of any length, from a single digit to the entire array, and it must read the same forward and backward.
"""

def largest_palindrome_substring(arr):
    def is_palindrome(start, end):
        while start < end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True

    max_length = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if is_palindrome(i, j):
                substring_length = j - i + 1
                if substring_length > max_length:
                    max_length = substring_length
    return max_length