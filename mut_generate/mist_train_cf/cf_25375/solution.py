"""
QUESTION:
Implement a function called `calculate` that takes three parameters: two integers `a` and `b`, and a character `c` representing a basic arithmetic operation. The function should perform the operation represented by `c` on `a` and `b` and return the result. The allowed operations are addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). If the operation is division, assume that `b` is non-zero. If an unsupported operation is provided, the function should not perform any operation and return an undefined value.
"""

def calculate(a: int, b: int, c: str) -> int:
    """
    Perform a basic arithmetic operation on two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (str): A character representing the operation to perform.
                 Allowed operations are '+', '-', '*', '/'.

    Returns:
        int: The result of the operation if the operation is supported, otherwise None.
    """
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        if b != 0:
            return a // b
    return None