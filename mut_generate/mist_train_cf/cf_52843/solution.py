"""
QUESTION:
Create a function `switch_case` that takes an integer `x` as input and performs different arithmetic operations based on its value. The function should support the following operations: 
- if `x` equals 1, add 2 to the input value
- if `x` equals 2, multiply the input value by 3
- if `x` equals 3, subtract 4 from the input value
- if `x` is any other value, return the error message "these values are not mapped" 

Implement a unit test to verify the correctness of the `switch_case` function for all the defined cases and the error case.
"""

def switch_case(x):
    cases = {
        1: lambda val: val + 2,
        2: lambda val: val * 3,
        3: lambda val: val - 4,
    }
    func = cases.get(x, "these values are not mapped")
    if callable(func):
        return func(x)
    else:
        return func