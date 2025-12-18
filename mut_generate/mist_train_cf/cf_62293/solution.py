"""
QUESTION:
Refine the `refine_calculation` function. 

The function takes in two lists, `ops` and `nums`. `ops` includes mathematical operators and `nums` contains numerical values. Supported operations are exponentiation (**), integer division (//), bitwise AND (&), bitwise OR (|), and bitwise XOR (^). 

Restrictions: 
- The `ops` list should always have one less element than the `nums` list. 
- Numbers can represent both positive and negative integers. 
- The `ops` list should contain at least one operator, and `nums` list should contain at least two numbers.
"""

def refine_calculation(ops, nums):
    """
    This function takes in two lists, ops and nums. ops includes mathematical operators and nums contains numerical values.
    The function then calculates a mathematical expression that is built combining both lists.

    The following advanced mathematical operations are supported:
    - Exponentiation ( ** )
    - Integer division ( // )
    - Bitwise AND ( & )
    - Bitwise OR ( | )
    - Bitwise XOR ( ^ )

    Assumptions and constraints:
    - The ops list should always have one less element than the nums list.
    - Numbers can represent both positive and negative integers.
    - The ops list should contain at least one operator, and nums list should contain at least two numbers.
    """
    result = nums[0]
    for i in range(len(ops)):
        if ops[i] == '**': result = result ** nums[i+1]
        elif ops[i] == '//': result = result // nums[i+1]
        elif ops[i] == '&': result = result & nums[i+1]
        elif ops[i] == '|': result = result | nums[i+1]
        elif ops[i] == '^': result = result ^ nums[i+1]
    return result