"""
QUESTION:
Write a function `check_divisibility(num)` that checks if the given integer `num` is divisible by 3, 5, 7, or 11 and prints a string according to the following rules:
- If `num` is divisible by all four, print "FizzBuzzWoofCrackle".
- If `num` is divisible by three of them, print "FizzBuzzWoof", "FizzBuzzCrackle", "FizzWoofCrackle", or "BuzzWoofCrackle" depending on the combination.
- If `num` is divisible by two of them, print "FizzBuzz", "FizzWoof", "FizzCrackle", "BuzzWoof", "BuzzCrackle", or "WoofCrackle" depending on the combination.
- If `num` is divisible by one of them, print "Fizz", "Buzz", "Woof", or "Crackle" depending on the divisor.
- If `num` is not divisible by any of them, print `num`.
"""

def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0 and num % 11 == 0:
        return "FizzBuzzWoofCrackle"
    elif num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        return "FizzBuzzWoof"
    elif num % 3 == 0 and num % 5 == 0 and num % 11 == 0:
        return "FizzBuzzCrackle"
    elif num % 3 == 0 and num % 7 == 0 and num % 11 == 0:
        return "FizzWoofCrackle"
    elif num % 5 == 0 and num % 7 == 0 and num % 11 == 0:
        return "BuzzWoofCrackle"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 7 == 0:
        return "FizzWoof"
    elif num % 3 == 0 and num % 11 == 0:
        return "FizzCrackle"
    elif num % 5 == 0 and num % 7 == 0:
        return "BuzzWoof"
    elif num % 5 == 0 and num % 11 == 0:
        return "BuzzCrackle"
    elif num % 7 == 0 and num % 11 == 0:
        return "WoofCrackle"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "Woof"
    elif num % 11 == 0:
        return "Crackle"
    else:
        return num