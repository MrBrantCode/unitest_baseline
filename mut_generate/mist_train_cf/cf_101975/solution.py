"""
QUESTION:
Create a function named `greet_and_check_palindrome` that takes a string as input. The input string should only contain alphabetic characters and have a length of 1 to 100 characters. The function should print an error message if the input string is invalid. Otherwise, it should print a greeting message with the input string, and an additional message indicating whether the input string is a palindrome or not.
"""

def greet_and_check_palindrome(string):
    if not string.isalpha() or len(string) < 1 or len(string) > 100:
        print("Error: Invalid input. The input should only contain alphabetic characters and be between 1 and 100 characters in length.")
        return
    
    print("Hello {}!".format(string))
    
    if string == string[::-1]:
        print("The input string is a palindrome.")
    else:
        print("The input string is not a palindrome.")