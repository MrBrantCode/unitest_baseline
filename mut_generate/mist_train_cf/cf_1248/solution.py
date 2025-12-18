"""
QUESTION:
Write a function `fizz_buzz_boom` that takes a list of integers `numbers` as input and returns a list of strings or integers. For each number, check if it is divisible by 3, 5, and 7, and append the corresponding string to the result list according to the following rules:
- If divisible by 3, 5, and 7, append "FizzBuzzBoom".
- If divisible by 3 and 7, append "FizzBoom".
- If divisible by 5 and 7, append "BuzzBoom".
- If divisible by 3, append "Fizz".
- If divisible by 5, append "Buzz".
- If divisible by 7, append "Boom".
- Otherwise, append the input number itself.
The input list length should not exceed 10^6 and the absolute value of each number should not exceed 10^9.
"""

def fizz_buzz_boom(numbers):
    result = []
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
            result.append("FizzBuzzBoom")
        elif number % 3 == 0 and number % 7 == 0:
            result.append("FizzBoom")
        elif number % 5 == 0 and number % 7 == 0:
            result.append("BuzzBoom")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        elif number % 7 == 0:
            result.append("Boom")
        else:
            result.append(number)
    return result