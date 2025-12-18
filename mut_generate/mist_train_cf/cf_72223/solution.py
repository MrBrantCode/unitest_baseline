"""
QUESTION:
Implement the function `calPoints(ops)` that takes a list of strings `ops` as input, where each string represents an operation to be executed on the record. The operations can be one of the following: an integer `x` to register a new score, `"+"` to register a new score that is the sum of the last two scores, `"D"` to register a new score that is twice the last score, or `"C"` to invalidate the last score. The function should return the total of all the scores on the record after executing all operations.
"""

def calPoints(ops):
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
    return sum(stack)