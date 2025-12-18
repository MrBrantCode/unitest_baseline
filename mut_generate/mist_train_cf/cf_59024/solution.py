"""
QUESTION:
Write a function named `bit_operations` that takes two binary strings `a` and `b` as input. The function should perform bitwise XOR, AND, and OR operations on these strings without using direct Boolean bitwise operations. It must manually compute these operations through logical programming constructs. The function should return a sequence of strings containing the results of the XOR, AND, and OR operations, respectively. The input strings may be of different lengths; pad the shorter string with zeros from the left to make them equal in length before performing the operations.
"""

def bit_operations(a, b):
    """
    This function takes two binary strings a and b as input, performs 
    bitwise XOR, AND, and OR operations on these strings without using 
    direct Boolean bitwise operations, and returns a sequence of strings 
    containing the results of the XOR, AND, and OR operations, respectively.
    
    :param a: Binary string
    :param b: Binary string
    :return: Sequence of strings containing the results of the XOR, AND, and OR operations
    """
    
    # Find the maximum length between the two input strings
    max_len = max(len(a), len(b))
    
    # Pad the shorter string with zeros from the left
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    # Initialize result strings with zeros
    xor_res = ['0'] * max_len
    and_res = ['0'] * max_len
    or_res = ['0'] * max_len
    
    # Perform bitwise operations
    for i in range(max_len):
        # XOR operation
        xor_res[i] = '1' if a[i] != b[i] else '0'
        
        # AND operation
        and_res[i] = '1' if a[i] == '1' and b[i] == '1' else '0'
        
        # OR operation
        or_res[i] = '1' if a[i] == '1' or b[i] == '1' else '0'
    
    # Return the results as a sequence of strings
    return [''.join(xor_res), ''.join(and_res), ''.join(or_res)]