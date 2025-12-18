"""
QUESTION:
Spoonerize... with numbers... numberize?... numboonerize?... noonerize? ...anyway!  If you don't yet know what a spoonerism is and haven't yet tried my spoonerism kata, please do [check it out](http://www.codewars.com/kata/spoonerize-me) first.

You will create a function which takes an array of two positive integers, spoonerizes them, and returns the positive difference between them as a single number or ```0``` if the numbers are equal:
```
[123, 456] = 423 - 156 = 267
```
Your code must test that all array items are numbers and return ```"invalid array"``` if it finds that either item is not a number.  The provided array will always contain 2 elements.

When the inputs are valid, they will always be integers, no floats will be passed.  However, you must take into account that the numbers will be of varying magnitude, between and within test cases.
"""

def noonerize(numbers):
    # Check if the input list contains exactly two elements and both are integers
    if len(numbers) != 2 or not all(isinstance(num, int) for num in numbers):
        return "invalid array"
    
    try:
        # Convert the first digit of the second number and the rest of the first number
        num1 = int(str(numbers[1])[0] + str(numbers[0])[1:])
        # Convert the first digit of the first number and the rest of the second number
        num2 = int(str(numbers[0])[0] + str(numbers[1])[1:])
    except ValueError:
        return "invalid array"
    
    # Return the positive difference between the two new numbers
    return abs(num1 - num2)