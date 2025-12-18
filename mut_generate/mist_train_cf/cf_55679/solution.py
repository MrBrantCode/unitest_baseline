"""
QUESTION:
Write a function named `second_largest_palindrome` that takes a string `s` as input and returns the second longest palindromic substring in `s`. If there is no second longest palindromic substring, return `None`.
"""

def second_largest_palindrome(s):
    all_palindromes = []
    for i in range(len(s)):
        for j in range(i,len(s)):
            substr = s[i:j+1]
            if substr == substr[::-1]: # If substring is a palindrome
                all_palindromes.append(substr)
                
    # Sort list of all palindromes by length in descending order
    all_palindromes.sort(key=len, reverse=True) 
        
    # Return second element in sorted list (next-to-maximum length palindrome)
    try:
        return all_palindromes[1]  # If there is a second longest palindrome
    except IndexError:
        return None  # If there's not a second longest palindrome