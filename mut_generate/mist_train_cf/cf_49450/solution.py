"""
QUESTION:
Create a function called `maximal_palindromic_integer` that takes in a list of integers and a list of prohibited digits. The function should return the maximum palindromic integer from the list that does not contain any of the prohibited digits. If no such integer exists, the function should return `None`. The prohibited digits should be passed as strings.
"""

def maximal_palindromic_integer(number_list, prohibited_digits):
    max_palindrome = None
    for num in number_list:
        if str(num) == str(num)[::-1] and not any(digit in str(num) for digit in prohibited_digits):
            if max_palindrome is None or num > max_palindrome:
                max_palindrome = num
    return max_palindrome