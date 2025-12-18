"""
QUESTION:
Write a function `prefix_to_postfix` that takes a string `prefix_exp` representing an arithmetic expression in prefix notation as input. The function should return a tuple containing the equivalent postfix notation and an error message if the prefix expression is invalid. The function should correct the prefix expression by ignoring any invalid characters and return the corrected postfix notation. The function should handle errors such as invalid characters, insufficient operands for an operator, and incorrect expression syntax.
"""

def prefix_to_postfix(prefix_exp):
    stack = []
    error = None

    # loop through the expression from right to left
    for i in reversed(range(len(prefix_exp))):
        if prefix_exp[i].isnumeric() or prefix_exp[i].isalpha():
            # pushing operands
            stack.append(prefix_exp[i])
        elif prefix_exp[i] in "*+-/":
            # for each operator pop two elements from the stack, append the operator to the result
            if len(stack) >= 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b + prefix_exp[i])
            else:
                error = "Invalid Expression"
                break
        else:
            error = "Invalid Character/Expression"
            break

    # if the stack is empty or contains more than one element, return error
    if error is None and len(stack) != 1:
        error = "Invalid Expression"

    postfix_exp = stack[0] if not error else ""

    return (postfix_exp, error)