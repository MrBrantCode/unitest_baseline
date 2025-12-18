"""
QUESTION:
Create a function named `perfect_and_palindrome(n)` that finds all perfect numbers that are also palindrome numbers within the range 1 to `n`. A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself), and a palindrome number is a number that remains the same when its digits are reversed. The function should return or print a list of such numbers.
"""

def perfect_and_palindrome(n):
    def is_perfect(num):
        sum1 = 0
        for i in range(1, num):
            if(num % i == 0):
                sum1 = sum1 + i
        return sum1 == num

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    perfect_palindromes = []
    for i in range(1, n+1):
        if is_perfect(i) and is_palindrome(i):
            perfect_palindromes.append(i)
    return perfect_palindromes