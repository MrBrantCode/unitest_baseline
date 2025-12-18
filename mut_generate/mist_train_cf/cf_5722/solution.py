"""
QUESTION:
Write a function `find_palindromic_numbers(n)` that identifies all palindromic numbers between 1 and a given number `n` (up to 1 billion) and returns a list of these palindromic numbers along with the largest palindromic number within the range. 

Implement the solution without using any built-in functions or libraries to check for palindromic numbers. Ensure the solution has a time complexity of O(n log n) and can handle numbers up to 1 billion efficiently without causing any memory issues.
"""

def find_palindromic_numbers(n):
    def is_palindrome(num):
        reverse = 0
        temp = num
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp = temp // 10
        return num == reverse

    palindromes = []
    largest_palindrome = 0
    for i in range(1, n+1):
        if is_palindrome(i):
            palindromes.append(i)
            if i > largest_palindrome:
                largest_palindrome = i
    return palindromes, largest_palindrome