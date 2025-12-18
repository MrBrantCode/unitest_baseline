"""
QUESTION:
Write a function named `generate_parentheses(n)` that generates all possible combinations of balanced parentheses for a given number of pairs `n`. The function should return a list of all possible combinations, where each combination is a string of balanced parentheses. The function must use recursion and ensure that the parentheses are balanced in terms of count, position, and nesting.
"""

def generate_parentheses(n):
    result = []
    def backtrack(curr_str, open_count, close_count):
        if len(curr_str) == 2*n:
            result.append(curr_str)
            return
        if open_count < n:
            backtrack(curr_str + '(', open_count + 1, close_count)
        if open_count > close_count:
            backtrack(curr_str + ')', open_count, close_count + 1)
    backtrack("", 0, 0)
    return result