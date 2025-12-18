"""
QUESTION:
Determine the result of the following function with bitwise operations and nested conditional statements. The function takes four integers as input and uses bitwise AND, OR, left shift, and right shift operators to determine the output.

Function name: Not specified, but it should be named according to its purpose. 
Input: Four integers a, b, c, and d.
Restrictions: Use bitwise operators and nested conditional statements to determine the output. 

The function should return "Yes" if ((a & b) << c) > d and (a | b) >> c <= d, "No" if ((a & b) << c) > d and (a | b) >> c > d, and "Maybe" if ((a & b) << c) <= d.
"""

def bitwise_operation_result(a, b, c, d):
    if ((a & b) << c) > d:
        if (a | b) >> c <= d:
            return "Yes"
        else:
            return "No"
    else:
        return "Maybe"