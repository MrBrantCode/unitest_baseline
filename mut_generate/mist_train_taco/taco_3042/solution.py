"""
QUESTION:
You are given an integer N that has exactly four digits in base ten. How many times does `2` occur in the base-ten representation of N?

Constraints

* 1000 \leq N \leq 9999

Input

Input is given from Standard Input in the following format:


N


Output

Print the answer.

Examples

Input

1222


Output

3


Input

3456


Output

0


Input

9592


Output

1
"""

def count_digit_two(N: int) -> int:
    # Convert the integer to a string to easily iterate over each digit
    str_N = str(N)
    
    # Initialize a counter for the digit '2'
    count = 0
    
    # Iterate over each character in the string representation of N
    for char in str_N:
        if char == '2':
            count += 1
    
    # Return the count of '2's
    return count