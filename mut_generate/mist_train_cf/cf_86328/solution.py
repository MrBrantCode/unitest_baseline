"""
QUESTION:
Implement a recursive function named `evaluate_expression` that evaluates a mathematical expression parsed from a string input, containing multiple operators and parentheses, and returns the result rounded to the nearest whole number. The function should not use loops or built-in arithmetic operators. The allowed operations are addition (+), subtraction (-), multiplication (*), and division (/). The time complexity should be O(log n) and the space complexity should be O(log n), where n is the value of the input expression.
"""

def evaluate_expression(expression):
    expression = expression.replace(" ", "")

    if expression.isdigit():
        return round(float(expression))

    closing_parenthesis_index = expression.find(")")

    if closing_parenthesis_index == -1:
        return evaluate_expression_helper(expression)

    opening_parenthesis_index = expression.rfind("(", 0, closing_parenthesis_index)
    sub_expression = expression[opening_parenthesis_index + 1: closing_parenthesis_index]
    sub_result = evaluate_expression_helper(sub_expression)
    new_expression = (
        expression[:opening_parenthesis_index]
        + str(sub_result)
        + expression[closing_parenthesis_index + 1:]
    )
    return evaluate_expression(new_expression)

def evaluate_expression_helper(expression):
    addition_index = expression.find("+")
    subtraction_index = expression.find("-")
    multiplication_index = expression.find("*")
    division_index = expression.find("/")

    if addition_index == -1 and subtraction_index == -1 and multiplication_index == -1 and division_index == -1:
        return round(float(expression))

    operator_index = min(
        index
        for index in [
            addition_index,
            subtraction_index,
            multiplication_index,
            division_index,
        ]
        if index != -1
    )

    left_expression = expression[:operator_index]
    right_expression = expression[operator_index + 1:]

    left_result = evaluate_expression_helper(left_expression)
    right_result = evaluate_expression_helper(right_expression)

    operator = expression[operator_index]
    if operator == "+":
        result = left_result + right_result
    elif operator == "-":
        result = left_result - right_result
    elif operator == "*":
        result = left_result * right_result
    elif operator == "/":
        result = left_result / right_result

    return round(result)