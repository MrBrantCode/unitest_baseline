"""
QUESTION:
Create a function `fetch_character` that takes a string and an integer `k` as parameters and returns the kth character of the string. The function should handle exceptions where the string has fewer characters than `k` or `k` is less than or equal to 0. The function should be case-sensitive and treat 'A' and 'a' as distinct characters. The index `k` should be 1-based, meaning the first character corresponds to `k = 1`.
"""

def fetch_character(string, k):
    try:
        if k > 0:
            return string[k-1]
        else:
            print("Error: k should be greater than 0")
    except IndexError:
        print("Error: string index out of range")