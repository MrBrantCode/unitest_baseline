"""
QUESTION:
Implement the `decode_energy_sums` function, which takes a 32-bit integer `buf` as input and returns a dictionary containing two decoded energy sums, 'trace_length' and 'trace_out_of_range'. The decoding scheme involves applying a bitwise AND operation between the input buffer and a specific mask for each energy sum, followed by a right shift operation using the value obtained from the mask.

The masks for 'trace_length' and 'trace_out_of_range' are (0xFFFF0000, 16) and (0x0000FFFF, 0) respectively. The function should return a dictionary where the keys are the names of the energy sums and the values are the decoded energy sums.
"""

def decode_energy_sums(buf: int) -> dict:
    mask = {
        'trace_length': (0xFFFF0000, 16),  
        'trace_out_of_range': (0x0000FFFF, 0)  
    }

    return {
        'trace_length': (buf & mask['trace_length'][0]) >> mask['trace_length'][1],
        'trace_out_of_range': (buf & mask['trace_out_of_range'][0]) >> mask['trace_out_of_range'][1]
    }