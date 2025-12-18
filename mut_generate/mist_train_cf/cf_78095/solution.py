"""
QUESTION:
Write a recursive function named `recursive_compare` that takes a list of comparisons as input, where each comparison is a list of three elements: the first operand, the operator, and the second operand. The function should return a list of boolean outputs corresponding to each comparison. Supported operators are '==', '<', '>', '<=', and '>='. The function should handle edge cases, including negative numbers and zero. If an invalid operator is encountered, the function should print an error message and return None for that comparison.
"""

def recursive_compare(list_of_comparisons):
    if not list_of_comparisons: 
        return []

    comparison = list_of_comparisons[0] 
    operand1 = comparison[0] 
    operator = comparison[1] 
    operand2 = comparison[2] 

    if operator == '==':
        result = operand1 == operand2
    elif operator == '<':
        result = operand1 < operand2
    elif operator == '>':
        result = operand1 > operand2
    elif operator == '<=':
        result = operand1 <= operand2
    elif operator == '>=':
        result = operand1 >= operand2
    else:
        print("Invalid operator") 
        result = None

    return [result] + recursive_compare(list_of_comparisons[1:]) 