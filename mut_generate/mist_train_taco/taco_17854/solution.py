"""
QUESTION:
You have to create a function which receives 3 arguments: 2 numbers, and the result of an unknown operation performed on them (also a number).

Based on those 3 values you have to return a string, that describes which operation was used to get the given result.

The possible return strings are:
  `"addition"`,
  `"subtraction"`,
  `"multiplication"`,
  `"division"`.

## Example:
```
calcType(1, 2, 3) -->   1 ? 2 = 3   --> "addition"
```

## Notes
* In case of division you should expect that the result of the operation is obtained by using `/` operator on the input values - no manual data type conversion or rounding should be performed.
* Cases with just one possible answers are generated.
* Only valid arguments will be passed to the function.
"""

def determine_operation(a, b, res):
    """
    Determines the operation that was performed on `a` and `b` to get `res`.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    res (int or float): The result of the operation performed on `a` and `b`.

    Returns:
    str: A string indicating the operation ("addition", "subtraction", "multiplication", or "division").
    """
    if a + b == res:
        return "addition"
    elif a - b == res:
        return "subtraction"
    elif a * b == res:
        return "multiplication"
    elif a / b == res:
        return "division"