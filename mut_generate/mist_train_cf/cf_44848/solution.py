"""
QUESTION:
Write a program that reads a file named "expressions.txt" containing simple arithmetic expressions, one per line, in the format "number operator number" (e.g. "2 + 3" or "4 * 5"), and writes each expression along with its result to a file named "output.txt" in the format "<expression> = <result>". Ensure proper handling of newline characters and file operations. The program should handle addition, subtraction, multiplication, and division, assuming no division by zero occurs.
"""

def entrance(expression):
    expression_parts = expression.split(' ')
    result = 0
    if expression_parts[1] == '+':
        result = float(expression_parts[0]) + float(expression_parts[2])
    elif expression_parts[1] == '-':
        result = float(expression_parts[0]) - float(expression_parts[2])
    elif expression_parts[1] == '*':
        result = float(expression_parts[0]) * float(expression_parts[2])
    elif expression_parts[1] == '/':
        result = float(expression_parts[0]) / float(expression_parts[2])
    return result