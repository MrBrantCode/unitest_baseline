"""
QUESTION:
Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya wonders eagerly what minimum lucky number has the sum of digits equal to n. Help him cope with the task.

Input

The single line contains an integer n (1 ≤ n ≤ 106) — the sum of digits of the required lucky number.

Output

Print on the single line the result — the minimum lucky number, whose sum of digits equals n. If such number does not exist, print -1.

Examples

Input

11


Output

47


Input

10


Output

-1
"""

def find_min_lucky_number(n: int) -> str:
    from collections import Counter
    
    # Counter for handling the remainder cases
    c = Counter({
        1: [-1, 2],
        2: [-2, 4],
        3: [-3, 6],
        4: [0, 1],
        5: [-1, 3],
        6: [-2, 5]
    })
    
    # Calculate the remainder and quotient when n is divided by 7
    a = n % 7
    s = n // 7
    f = 0
    
    if a == 0:
        # If the remainder is 0, the number can be formed entirely by '7's
        return '7' * s
    else:
        # Adjust the number of '7's and '4's based on the remainder
        s += c[a][0]
        f += c[a][1]
        
        if s < 0:
            # If the number of '7's becomes negative, check if the number can be formed by '4's
            if n % 4 == 0:
                return '4' * (n // 4)
            else:
                return '-1'
        else:
            # Form the lucky number with the calculated number of '4's and '7's
            return '4' * f + '7' * s