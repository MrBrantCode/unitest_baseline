"""
QUESTION:
[Image] 


-----Input-----

The input contains two integers a_1, a_2 (0 ≤ a_{i} ≤ 32), separated by a single space.


-----Output-----

Output a single integer.


-----Examples-----
Input
1 1

Output
0

Input
3 7

Output
0

Input
13 10

Output
1
"""

def reverse_and_add(a_1: int, a_2: int) -> int:
    # Convert the second number to a string
    b_str = str(a_2)
    
    # Reverse the string representation of the second number
    reversed_b_str = b_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_b = int(reversed_b_str)
    
    # Add the first number to the reversed second number
    result = a_1 + reversed_b
    
    return result