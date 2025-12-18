"""
QUESTION:
Petya loves lucky numbers. Everybody knows that positive integers are lucky if their decimal representation doesn't contain digits other than 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Lucky number is super lucky if it's decimal representation contains equal amount of digits 4 and 7. For example, numbers 47, 7744, 474477 are super lucky and 4, 744, 467 are not.

One day Petya came across a positive integer n. Help him to find the least super lucky number which is not less than n.

Input

The only line contains a positive integer n (1 ≤ n ≤ 10100000). This number doesn't have leading zeroes.

Output

Output the least super lucky number that is more than or equal to n.

Examples

Input

4500


Output

4747


Input

47


Output

47
"""

from itertools import permutations as p

def find_least_super_lucky_number(n: str) -> str:
    def ck(num, arr):
        for i in arr:
            if i >= num:
                return str(i)
        return None

    z = len(n)
    if z == 1:
        return "47"
    elif z == 2:
        if int(n) <= 74:
            arr = [47, 74]
            return ck(int(n), arr)
        else:
            return "4477"
    elif z == 3:
        return "4477"
    elif z == 4:
        if int(n) <= 7744:
            arr4 = sorted([int(''.join(i)) for i in p('4477')])
            return ck(int(n), arr4)
        else:
            return "444777"
    elif z == 5:
        return "444777"
    elif z == 6:
        if int(n) <= 777444:
            arr6 = sorted([int(''.join(i)) for i in p('444777')])
            return ck(int(n), arr6)
        else:
            return "44447777"
    elif z == 7:
        return "44447777"
    elif z == 8:
        if int(n) <= 77774444:
            arr8 = sorted([int(''.join(i)) for i in p('44447777')])
            return ck(int(n), arr8)
        else:
            return "4444477777"
    else:
        return "4444477777"