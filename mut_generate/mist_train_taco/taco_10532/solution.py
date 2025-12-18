"""
QUESTION:
Problem

If you bring an empty bottle of $ a $ milk, you can exchange it for a new bottle of $ b $ milk.
How many bottles of milk can Mr. Kawabayashi, who initially has a bottle of $ x $ milk, drink? Output the remainder after dividing by $ 1000000007 $.

Constraints

The input satisfies the following conditions.

* $ 1 \ leq a \ leq 10 ^ {15} $
* $ 0 \ leq b \ lt a $
* $ 0 \ leq x \ leq 10 ^ {15} $

Input

The input is given in the following format.


$ a $ $ b $ $ x $


Three integers $ a $, $ b $, $ x $ are given, separated by spaces.

Output

Print the answer on one line.

Examples

Input

3 1 5


Output

7


Input

3 2 5


Output

11


Input

82 69 64


Output

64


Input

316250877917604 316250877917599 681260158257385


Output

62687552
"""

def calculate_total_milk_drunk(a: int, b: int, x: int) -> int:
    MOD = 1000000007
    total_milk = x + max(0, x - b) // (a - b) * b
    return total_milk % MOD