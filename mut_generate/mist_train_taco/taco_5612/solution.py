"""
QUESTION:
The Enigma crew came to know some of the location where the bombs are planted. So they started to find the code through which they can diffuse the bombs .Each bomb has different code for diffusion. The crew found the solution the diffusion code is between the ranges 1 to N-1 where N is the integer value. The summation of the multiple of 3 or 5 within the range give the diffusion code.

Input Format
It contain the integer N.

Output Format
Print an integer that denotes the sum of all the multiples of 3 or 5 below N.

Constraints
1 ≤ N ≤ 10000000000

SAMPLE INPUT
10

SAMPLE OUTPUT
23
"""

def calculate_diffusion_code(N):
    def ap(n):
        return (n * (n + 1)) // 2
    
    if N <= 1:
        return 0
    
    return (ap((N - 1) // 3) * 3 + ap((N - 1) // 5) * 5 - ap((N - 1) // 15) * 15)