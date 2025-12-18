"""
QUESTION:
Write a function named `find_palindromes(n)` that takes an integer `n` as input and returns a list of all integer-based palindromes between 1 and `n`. The function should check each integer in this range to see if it's a palindrome by comparing the integer with its reverse.
"""

def find_palindromes(n):
    palindrome_list = []
    for i in range(1, n+1): 
        if str(i) == str(i)[::-1]: 
            palindrome_list.append(i) 
    return palindrome_list