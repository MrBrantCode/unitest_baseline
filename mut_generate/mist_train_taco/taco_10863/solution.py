"""
QUESTION:
Rohit was doing the work of his math class about three days but he is tired of make operations a lot and he should deliver his task tomorrow. His math’s teacher gives two numbers a and b. The problem consist in find the last digit of the potency of base a and index b. Help Rohit with his problem. You are given two integer numbers: the base a (number of digits d, such that 1 ≤ d ≤ 1000) and the index b (0 ≤ b ≤ 922*10^15). You
have to find the last digit of a^b.

Input

The first line of input contains an integer t, the number of test cases (t ≤ 30). t test cases follow. For each test case will appear a and b separated by space.

Output

For each test case output an integer per line representing the result.

SAMPLE INPUT
3
3 10
6 2
150 53

SAMPLE OUTPUT
9
6
0
"""

def find_last_digit_of_power(a: int, b: int) -> int:
    # Extract the last digit of the base 'a'
    last_digit_a = a % 10
    
    # Handle special cases where the exponent 'b' is 0
    if b == 0:
        return 1
    
    # Use patterns in the last digits of powers to optimize the calculation
    # The last digit of powers follows a repeating pattern for any base 'a'
    # For example, the last digits of powers of 2 follow the pattern: 2, 4, 8, 6
    # We can use this pattern to find the last digit of a^b efficiently
    
    # Define the repeating patterns for the last digits of powers
    patterns = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    
    # Get the pattern for the last digit of 'a'
    pattern = patterns[last_digit_a]
    
    # Find the position in the pattern based on the exponent 'b'
    # The length of the pattern is used to determine the position
    position = (b - 1) % len(pattern)
    
    # Return the last digit from the pattern
    return pattern[position]