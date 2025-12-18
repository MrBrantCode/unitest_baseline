"""
QUESTION:
Create a function `perform_algebra` that takes two lists as input: `operators` and `operands`. The `operators` list should contain strings representing mathematical operations (+, -, *, /, //, **, %) and the `operands` list should contain integers (positive or negative). The function should perform the operations in the order they appear in the lists, using each operand in sequence. If the lists are empty, return `None`.
"""

def perform_algebra(operators, operands):
    """
    Perform algebraic operations in the order they are present in the operators and operands list.
    Possible operators include addition, subtraction, multiplication, division, modulus, and power.
    The operators and operands lists could be empty or could contain multiple items.
    Also, an extra modulus function has been added amongst the operators.
    Operands can be negative and positive integers.
    Negative unary operators will be preceded by a zero in the operands list.
    This function does not handle standard order of operations (PEMDAS/BODMAS), it only computes sequentially.
    """
    if not operators or not operands:
        return None

    result = operands[0]
    for i in range(0, len(operators)):
        op = operators[i]
        num = operands[i+1]
        if op == "+":
            result += num
        elif op == "-":
            result -= num
        elif op == "*":
            result *= num
        elif op == "/":
            result /= num
        elif op == "//":
            result //= num
        elif op == "**":
            result **= num
        elif op == "%":
            result %= num
        else:
            return "Invalid operator found: {0}".format(op)

    return result