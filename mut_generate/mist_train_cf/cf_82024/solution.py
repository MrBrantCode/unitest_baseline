"""
QUESTION:
Create a function called `check_number(n)` that takes one argument `n` and returns a string indicating the category of the number. The function should categorize numbers into 'zero', 'one', 'prime', 'composite', 'negative', 'fractional', or 'not a number' based on the following rules: 

- 'zero' if n is 0
- 'one' if n is 1
- 'prime' if n is a prime number
- 'composite' if n is a composite number
- 'negative' if n is less than 0
- 'fractional' if n is a float number that is not a whole number
- 'not a number' if n is not a number or is a complex number

The function should handle inputs of different data types and return 'not a number' if the input is not a number.
"""

def check_number(n):
    try:
        if isinstance(n, str) or isinstance(n, complex) :
            return 'Not a number'
        elif n < 0 :
            return 'Negative'
        elif n == 0:
            return 'Zero'
        elif n == 1:
            return 'One'
        elif n%1 != 0 :
            return 'Fractional'
        else:
            n = int(n)
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return 'Composite'
            return 'Prime'
    except TypeError:
        return 'Not a number'