"""
QUESTION:
Joisino wants to evaluate the formula "A op B".
Here, A and B are integers, and the binary operator op is either + or -.
Your task is to evaluate the formula instead of her.

-----Constraints-----
 - 1≦A,B≦10^9
 - op is either + or -.

-----Input-----
The input is given from Standard Input in the following format:
A op B

-----Output-----
Evaluate the formula and print the result.

-----Sample Input-----
1 + 2

-----Sample Output-----
3

Since 1 + 2 = 3, the output should be 3.
"""

def evaluate_formula(A: int, op: str, B: int) -> int:
    if op == '+':
        return A + B
    elif op == '-':
        return A - B
    else:
        raise ValueError("Invalid operator. Only '+' and '-' are supported.")