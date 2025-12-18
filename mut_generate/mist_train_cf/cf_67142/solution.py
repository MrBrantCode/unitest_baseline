"""
QUESTION:
Write a function named `gen_mult_table` that takes three parameters: `m` and `n` which represent the dimensions of the multiplication table, and `format_type` which defaults to `'table'`. The function should either print the multiplication table or return a list of tuples, each containing the two operands and their product, depending on the value of `format_type`. If `format_type` is not `'table'` or `'tuples'`, the function should print an error message.
"""

def gen_mult_table(m, n, format_type='table'):
    if format_type == 'table':
        # If the user wants the result in table format
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(f'{i * j}', end='\t')
            print()
    elif format_type == 'tuples':
        # If the user wants the result in tuples format
        tuples_list = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                tuples_list.append((i, j, i * j))
        return tuples_list
    else:
        print("Invalid format type. Choose either 'table' or 'tuples'")