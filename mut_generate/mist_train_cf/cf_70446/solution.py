"""
QUESTION:
Implement a function named 'recursive_foo' that takes an integer 'x' and a list 'lst' of integers as parameters. The function should follow these rules: 

- If 'lst' is empty, return 'x'.
- If the first element of 'lst' is positive, add 'x' with the first element and recursively call 'recursive_foo' with the updated 'x' and the rest of 'lst'.
- If the first element of 'lst' is not positive, multiply 'x' by the first element and recursively call 'recursive_foo' with the updated 'x' and the rest of 'lst'.

The function should be called with an initial 'x' of 1 and a list containing at least 3 integers.
"""

def recursive_foo(x: int, lst: list) -> int:
    if not lst:
        return x
    else:
        head, *tail = lst
        if head > 0:
            return recursive_foo(x + head, tail)
        else:
            return recursive_foo(x * head, tail)