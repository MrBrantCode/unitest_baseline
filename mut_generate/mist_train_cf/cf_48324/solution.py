"""
QUESTION:
Write a function `count_palindromes(s)` that takes a string `s` as input and returns the total count of all unique substrings that are palindromes, including single characters, and the list of these palindromes. The function should consider all possible substrings of the input string, without any restrictions on their length.
"""

def is_palindrome(s):  
    return s == s[::-1]


def count_palindromes(s):  
    length = len(s)
    palindromes = set()  

    for i in range(length):  
        for j in range(i+1, length+1):  
            substr = s[i:j]  
            if is_palindrome(substr):  
                palindromes.add(substr)  

    return len(palindromes), list(palindromes)