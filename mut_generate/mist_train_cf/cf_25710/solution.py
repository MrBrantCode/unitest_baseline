"""
QUESTION:
Design a function named `evaluate` to take a string expression as input, which contains two numbers separated by a '+' operator. The function should add the two numbers and return the result as a float. The input string may contain spaces.
"""

def evaluate(expression):
  expr = expression.replace(" ","")
  expr_list = expr.split("+")
  result = float(expr_list[0]) + float(expr_list[1])
  return result