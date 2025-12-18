"""
QUESTION:
Create a program with two functions: `modulus(a, b)` and `list_modulus(pairs)`. The `modulus(a, b)` function calculates the modulus of two numbers, `a` and `b`, and returns an error message if `b` is zero. The `list_modulus(pairs)` function calculates the modulus for each pair of numbers in the list `pairs` using the `modulus(a, b)` function, prints an error message for any pair with a second number as zero, and prints all the successfully calculated modulus results. The modulus calculation should work with negative numbers and follow the rule that the result has the same sign as the divisor.
"""

def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error: Division by zero"

def list_modulus(pairs):
    results = []
    for pair in pairs:
        result = modulus(pair[0], pair[1])
        if type(result) == str:
            print(f"For pair {pair}, {result}")
        else:
            results.append(result)
    print(f"Modulus results: {results}")