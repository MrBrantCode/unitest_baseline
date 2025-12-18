"""
QUESTION:
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.
```if-not:csharp
if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
```
```if:csharp
If the sign is not a valid sign, throw an ArgumentException.
```

# Example:

```python
calculator(1, 2, '+') => 3
calculator(1, 2, '$') # result will be "unknown value"
```

Good luck!
"""

def calculate(x, y, op):
    # Check if x and y are numbers
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "unknown value"
    
    # Check if op is a valid operation
    if op not in ['+', '-', '*', '/']:
        return "unknown value"
    
    # Perform the operation
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        # Handle division by zero
        if y == 0:
            return "unknown value"
        return x / y