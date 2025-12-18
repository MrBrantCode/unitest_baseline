"""
QUESTION:
Given a single positive integer x and a target value, write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). Find the least number of operators used to express the target value, following the conventions: division returns rational numbers, no parentheses are used, and the usual order of operations applies. The expression cannot contain consecutive division operators and cannot use the unary negation operator (-). The function should take x and target as input and return the least number of operators used. Constraints: 2 <= x <= 100 and 1 <= target <= 2 * 10^8.
"""

def leastOpsExpressTarget(x: int, target: int) -> int:
    pos, neg, k, pos2, neg2 = 0, 0, 0, 0, 0
    while target:
        target, cur = divmod(target, x)
        if k:
            pos2, neg2 = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
        else:
            pos2, neg2 = cur * 2, (x - cur) * 2
        pos, neg, k = pos2, neg2, k + 1
    return min(pos, k + neg) - 1