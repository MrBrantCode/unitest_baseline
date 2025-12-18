"""
QUESTION:
Write a function `generate_parentheses(n)` that generates all possible combinations of `n` pairs of balanced parentheses. The function should return a list of strings, where each string is a combination of `n` pairs of balanced parentheses. The function should use a recursive approach and ensure that the parentheses are balanced not only in terms of count, but also in terms of position and nesting. The function should not take any additional arguments other than `n`, which is the number of pairs of parentheses.
"""

def generate_parentheses(n):
    def backtrack(curr_str, open_count, close_count, result):
        if len(curr_str) == 2*n:
            result.append(curr_str)
            return

        if open_count < n:
            backtrack(curr_str + '(', open_count + 1, close_count, result)

        if open_count > close_count:
            backtrack(curr_str + ')', open_count, close_count + 1, result)

    result = []
    backtrack("", 0, 0, result)
    return result