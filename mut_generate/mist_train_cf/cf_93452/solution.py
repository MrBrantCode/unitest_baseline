"""
QUESTION:
Create a function `exclusive_truth_table` that takes an integer `n` as input, representing the number of variables in the truth table. Using only bitwise operators, generate a truth table that represents the XOR operation for `n` input variables, and return the table as a list of tuples. The table should contain all possible input combinations and their corresponding XOR operation outputs.
"""

def exclusive_truth_table(n):
    """
    Generate a truth table representing the XOR operation for n input variables.
    
    Args:
        n (int): The number of variables in the truth table.
    
    Returns:
        list: A list of tuples containing all possible input combinations and their corresponding XOR operation outputs.
    """
    truth_table = []
    for i in range(2 ** n):
        inputs = [(i >> j) & 1 for j in range(n)]
        output = sum(inputs) % 2  # XOR operation
        truth_table.append(tuple(inputs + [output]))
    return truth_table