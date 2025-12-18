"""
QUESTION:
Write a function `valid24` that takes a list of four integers from 1 to 9 as input and returns `True` if it is possible to use the numbers along with the operators `*`, `/`, `+`, `-`, `(`, `)` to get the resultant value 24, and `False` otherwise. The `/` operator signifies real division, not integer division, and each operation is performed between two numbers. The `-` operator cannot be used as a unary operator, and concatenation of numbers is not allowed.
"""

import itertools
import fractions

def valid24(nums):
    def evaluate(a, op, b):
        if a is False or b is False: 
            return False
        if op == '+': 
            return a + b
        if op == '-': 
            return a - b
        if op == '*': 
            return a * b
        if op == '/': 
            return a / b if b != 0 else False

    def pairOperations(numbers, operations):
        a, op, b, op2, c, op3, d = numbers[0], operations[0], numbers[1], operations[1], numbers[2], operations[2], numbers[3]
        return evaluate(evaluate(evaluate(a, op, b), op2, c), op3, d)

    for nums in itertools.permutations(map(fractions.Fraction, nums)):
        for ops in itertools.product('+-*/', repeat=3):
            if pairOperations(nums, ops) == 24: 
                return True 
    return False