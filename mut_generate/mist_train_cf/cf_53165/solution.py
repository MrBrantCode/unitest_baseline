"""
QUESTION:
Construct a function `find_palindromes(n)` that takes an integer `n` as input and returns a list of numerical palindromes between 1 and `n` (inclusive). A numerical palindrome is a number that remains the same when its digits are reversed.
"""

def find_palindromes(n):
    palindromes = []
    for num in range(1, n + 1):
        str_num = str(num)
        if str_num == str_num[::-1]:
            palindromes.append(int(str_num))
    return palindromes