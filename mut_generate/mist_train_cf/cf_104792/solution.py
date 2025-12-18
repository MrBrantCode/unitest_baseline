"""
QUESTION:
Write a function `convert_array` that takes an array of integers as input and returns a string where each integer is replaced with a specific string according to the following rules:
- If the integer is divisible by both 4 and 5, replace with "FizzBuzzFizzBuzz".
- If the integer is divisible by both 2 and 3, replace with "FizzBuzz".
- If the integer is divisible by 2, replace with "Fizz".
- If the integer is divisible by 3, replace with "Buzz".
- If the integer is divisible by 4, replace with "FizzBuzzFizz".
- If the integer is divisible by 5, replace with "BuzzFizzBuzz".
- If none of the above conditions are met, replace with the integer as a string.
"""

def convert_array(arr):
    output = ""
    for num in arr:
        if num % 4 == 0 and num % 5 == 0:
            output += "FizzBuzzFizzBuzz "
        elif num % 2 == 0 and num % 3 == 0:
            output += "FizzBuzz "
        elif num % 2 == 0:
            output += "Fizz "
        elif num % 3 == 0:
            output += "Buzz "
        elif num % 4 == 0:
            output += "FizzBuzzFizz "
        elif num % 5 == 0:
            output += "BuzzFizzBuzz "
        else:
            output += str(num) + " "
    
    return output