"""
QUESTION:
Create a function `nth_largest_palindrome(lst, n)` that takes a list of integers `lst` and an integer `n` as input, and returns the Nth largest palindrome number in the list. A palindrome number is a number that remains the same when its digits are reversed. If there are less than `n` palindrome numbers in the list, the function should return "Not enough palindromes in the list."
"""

def nth_largest_palindrome(lst, n):
    def is_palindrome(num):
        return str(num) == str(num)[::-1]
    
    palindromes = sorted([x for x in lst if is_palindrome(x)], reverse=True)
    if len(palindromes) < n:
        return "Not enough palindromes in the list."
    else:
        return palindromes[n-1]