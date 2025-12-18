"""
QUESTION:
Implement a function `rearrange_on_operations(operations_string, nums_list)` that takes a string of comma-separated operation names and a list of integers, applies the operations to the list, and returns a dictionary where each key is an operation and the value is the sorted list of integers resulting from that operation. The function should handle the operations 'divN' (division by a custom number), 'pow2' (squaring), 'addN' (adding a custom number), and 'sqrt' (calculating the square root), replacing unfeasible outputs with 'Error' and incorporating exception handling for potential unforeseen errors.
"""

def rearrange_on_operations(operations_string, nums_list):
    operations_list = operations_string.split(',')
    operations_dict = {}
    possible_operations = ['div', 'pow2', 'add', 'sqrt']

    for operation in operations_list:
        if any(op in operation for op in possible_operations):
            try:
                if 'div' in operation:
                    divisor = int(operation.replace('div',''))
                    new_list = ['Error' if divisor == 0 else num/divisor for num in nums_list]
                elif operation == 'pow2':
                    new_list = [num**2 for num in nums_list]
                elif 'add' in operation:
                    adder = int(operation.replace('add',''))
                    new_list = [num + adder for num in nums_list]
                elif operation == 'sqrt':
                    new_list = ['Error' if num < 0 else num**0.5 for num in nums_list]
                operations_dict[operation] = sorted(new_list)
            except Exception as err:
                return f'Error occurred: {err}'
    return operations_dict