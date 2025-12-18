"""
QUESTION:
Implement a function `calculate_cigar_operations` that takes four parameters: `length`, `query_sequence`, `reference_sequence`, and `alignment`. The function should return a list of tuples representing the CIGAR operations based on the given sequences and alignment operations.

The `alignment` parameter contains tuples of the form `(operation, length)`, where `operation` is one of `MATCH`, `INSERTION`, or `DELETION` and `length` is the number of bases involved in that operation. The function should return a list of tuples, where each tuple represents an operation-length pair in the CIGAR string.
"""

def calculate_cigar_operations(length, query_sequence, reference_sequence, alignment):
    cigar_operations = []
    query_index = 0
    for operation, op_length in alignment:
        if operation == 'MATCH':
            cigar_operations.append(('M', op_length))
            query_index += op_length
        elif operation == 'INSERTION':
            cigar_operations.append(('I', op_length))
            query_index += op_length
        elif operation == 'DELETION':
            cigar_operations.append(('D', op_length))
    return cigar_operations