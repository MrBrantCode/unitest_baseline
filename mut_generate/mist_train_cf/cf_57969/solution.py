"""
QUESTION:
Create a function named `operations` that takes a string of comma-separated arithmetic operations (`ops_str`) and a list of integers (`numbers`). The function applies the operations sequentially to each number in the list. The allowed operations are 'div3' (divide by 3), 'pow2' (square the number), and 'add5' (add 5). The order of operations matters. The function should return the new list of numbers after applying all operations.
"""

def operations(ops_str, numbers):
    operations_mapping = {
        'div3': lambda x: x / 3,
        'pow2': lambda x: x**2,
        'add5': lambda x: x + 5,
    }

    operations = ops_str.split(',')
    new_numbers = numbers[:]
    for op_str in operations:
        operation = operations_mapping[op_str]
        new_numbers = [operation(n) for n in new_numbers]

    return new_numbers