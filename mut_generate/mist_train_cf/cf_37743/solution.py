"""
QUESTION:
Create a function named `fizz_buzz` that takes a list of integers as input and returns a modified list where numbers are replaced according to the following rules: 
- If a number is divisible by both 3 and 5, replace it with "FizzBuzz".
- If a number is divisible by 3, replace it with "Fizz".
- If a number is divisible by 5, replace it with "Buzz".
- If a number is not divisible by either 3 or 5, keep it unchanged.

The function should return a list that can contain both integers and strings.
"""

from typing import List, Union

def fizz_buzz(numbers: List[int]) -> List[Union[int, str]]:
    result = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)
    return result