"""
QUESTION:
Write a function `find_greatest_diff_and_perform_operation` that takes a list of tuples, where each tuple contains a list of numbers and an operator (+, -, *, /). The function should return a new list where each element is the result of performing the given operation on the greatest difference between any two numbers from the corresponding list in the tuple. Assume the lists will always have at least two elements and the operations are feasible (i.e., there will be no division by zero).
"""

def find_greatest_diff_and_perform_operation(list_tuples):
    result = []
    for l, op in list_tuples:
        min_val = min(l)
        max_val = max(l)
        diff = max_val - min_val

        if op == '+':
            result.append(diff + diff)
        elif op == '*':
            result.append(diff * diff)
        elif op == '-':
            result.append(diff - diff)
        elif op == '/':
            result.append(1)  # since dividing any number by itself gives 1
    return result