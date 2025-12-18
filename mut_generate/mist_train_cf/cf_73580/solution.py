"""
QUESTION:
You are given a chemical formula as a string. The task is to return a count of each individual atom present in the formula. The output should be a string where the elements are sorted and each count is appended to its element if the count is more than 1. Implement the function `countOfAtoms(formula)` where `formula` consists of English letters, digits, '(', and ')', and its length is between 1 and 1000, inclusive.
"""

import re
import collections

def countOfAtoms(formula):
    i, n = 0, len(formula)
    stack = [collections.Counter()]
    while i < n:
        if formula[i] == '(':
            stack.append(collections.Counter())
            i += 1
        elif formula[i] == ')':
            top = stack.pop()
            i += 1
            j = i
            while i < n and formula[i].isdigit():
                i += 1
            multi = int(formula[j:i] or 1)

            for name, v in top.items():
                stack[-1][name] += v * multi
        else:
            j = i + 1
            while j < n and formula[j].islower():
                j += 1
            name = formula[i:j]
            i = j

            j = i
            while i < n and formula[i].isdigit():
                i += 1
            multi = int(formula[j:i] or 1)
            stack[-1][name] += multi

    return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                   for name in sorted(stack[-1]))