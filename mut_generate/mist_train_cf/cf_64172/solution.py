"""
QUESTION:
Create a function named `check_palindrome` that takes a string `data` as input. The function should reverse the input string, check if it's a palindrome, and return the mid-point character or characters if it is a palindrome. If the string is not a palindrome, the function should return False. The function should be efficient and have a low time complexity.
"""

def check_palindrome(data):
    if data == data[::-1]:
        length = len(data)
        if length % 2 == 0:
            mid = data[length//2-1:length//2+1]
        else:
            mid = data[length//2]
        return mid
    else:
        return False