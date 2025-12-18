"""
QUESTION:
Write a function `largest_palindrome_product(n)` that takes an integer `n` as input, where `n` represents the number of digits in each of the two numbers to be multiplied. The function should return the largest palindrome that can be obtained by multiplying two `n`-digit numbers.
"""

def largest_palindrome_product(n):
    max_num = int('9' * n)
    min_num = int('1' + '0' * (n - 1))
    largest_palindrome = 0

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            temp = i * j
            if temp <= largest_palindrome:
                break
            if str(temp) == str(temp)[::-1]:
                largest_palindrome = temp
                break

    return largest_palindrome