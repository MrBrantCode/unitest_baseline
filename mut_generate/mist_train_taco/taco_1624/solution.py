"""
QUESTION:
See Russian Translation

The statement of this problem is quite short , apt and clear. We don't want any coder to spend time in reading a lengthy, boring story that has no connection with the actual problem. 

The problem states:

Given a pair (1,1), your aim is to get a new pair (a,b) in minimum number of operations.

There are two types of operations you can use: 

1.)  If the pair is ( x , y ) then change it to ( x+y, y )

2.)  If the pair is ( x , y ) then change it to ( x, x+y )

It is guaranteed that a and b are co-prime .

Input:

The first line contains the number of test cases T. 
Then, T lines follow, where each line contains a and b respectively. 

Output:

Print a line containing the minimum number of operations required to achieve the given fraction, corresponding to each test case. 

Constraints:

1 ≤ T ≤10 

1 ≤ a,b ≤10^18

a and b are co-primes

SAMPLE INPUT
2 
1 1
5 2

SAMPLE OUTPUT
0 
3
"""

def calculate_min_operations(a: int, b: int) -> int:
    """
    Calculate the minimum number of operations required to transform the pair (1, 1) into (a, b).

    Parameters:
    a (int): The first integer of the target pair.
    b (int): The second integer of the target pair.

    Returns:
    int: The minimum number of operations required.
    """
    count = 0
    while True:
        if a == 1 and b == 1:
            break
        if a == 1:
            count += b - 1
            break
        if b == 1:
            count += a - 1
            break
        
        if a > b:
            count += a // b
            a = a % b
        else:
            count += b // a
            b = b % a
        
        if a == 0 or b == 0:
            break
    
    return count