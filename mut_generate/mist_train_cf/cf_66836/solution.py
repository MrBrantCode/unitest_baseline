"""
QUESTION:
Write a recursive function `find_palindromes` that takes a string and two indices, start and end, as parameters. It should return all possible palindromes created by reversing different substrings of the given string. The function should use memoization to prevent recalculating already reversed substrings. The function should also be able to handle cases where start is greater than or equal to end, and should return an empty list in such cases.
"""

def find_palindromes(s, start, end, memo):
    if start >= end:
        return []
        
    if (start, end) in memo:
        return memo[(start, end)]

    reversed_string = s[start:end + 1][::-1]
    if reversed_string == reversed_string[::-1]:
        palindromes = [reversed_string]
    else:
        palindromes = []

    palindromes.extend(find_palindromes(s, start+1, end, memo))
    palindromes.extend(find_palindromes(s, start, end-1, memo))

    memo[(start, end)] = palindromes
    return palindromes