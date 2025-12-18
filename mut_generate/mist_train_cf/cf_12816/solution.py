"""
QUESTION:
Write a function called `find_palindromic_numbers` that takes an integer `n` as input, where `n` can be up to 1 million, and returns a list of palindromic numbers between 1 and `n`. The solution should not use any built-in functions or libraries to check for palindromic numbers and should have a time complexity of O(n log n).
"""

def find_palindromic_numbers(n):
    def is_palindrome(num):
        reversed_num = 0
        temp = num

        while temp > 0:
            reversed_num = (reversed_num * 10) + (temp % 10)
            temp //= 10

        return reversed_num == num

    palindromic_numbers = [num for num in range(1, n + 1) if is_palindrome(num)]
    return palindromic_numbers