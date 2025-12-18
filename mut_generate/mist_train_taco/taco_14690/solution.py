"""
QUESTION:
Given a binary number (of $N$ bits) $X$. Find the highest power of 2 that divides this number.
Note: If the binary number is "100" then the highest power of 2 that divides it is 2 (as $2^{2}$ = 4)

------ Input: ------ 

The first line contains N the number of bits in the number
The next line contains a binary number of N bits

------ Output: ------ 

The first and only line contains the max power of 2 that divides the given number

------ Constraints: ------ 

$ $1 ≤ N ≤10^{5}$$
$ $1≤ X$$

----- Sample Input 1 ------ 
5
10100
----- Sample Output 1 ------ 
2
"""

def find_max_power_of_2_divisor(N: int, X: str) -> int:
    # Convert the binary string to an integer
    t = int(X, 2)
    c = 0
    
    # Iterate to find the highest power of 2 that divides the number
    for i in range(1, N + 1):
        if t % (2 ** i) == 0:
            c = i
        else:
            break
    
    return c