"""
QUESTION:
Write a function `evaluate_expressions(n, expressions)` that takes an integer `n` and a list of `n` mathematical expressions as strings, where '^' represents exponentiation. Replace '^' with '**' in each expression, evaluate it, and return a list of strings with the results. If an expression is invalid or cannot be evaluated, return "Invalid expression" for that expression.
"""

def evaluate_expressions(n, expressions):
    results = []
    for exp in expressions:
        try:
            exp = exp.replace('^', '**')
            result = eval(exp)
            results.append(str(result))
        except:
            results.append("Invalid expression")
    return results