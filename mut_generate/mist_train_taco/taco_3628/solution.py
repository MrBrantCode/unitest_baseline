"""
QUESTION:
Beri is standing at co-ordinate (0,0).
He wants to go to the library.
Library is located at co-ordinate (N,0).
He wants to go to library by taking several jumps.
He can jump from co-ordinate (a,0) to (b,0) only if |b-a| can be expressed in the powers of 2. i.e, 2^m=|b-a| , for some integer m(m ≥ 0).
As he is very lazy he won't take many jumps.
Help him to find the minimum number of jumps required to reach the destination.

Example :
N=27
he will jump 1 steps , he will reach (1,0)
he will jump 2 steps , he will reach (3,0)
he will jump 8 steps , he will reach (11,0)
he will jump 16 steps, he will reach (27,0)
so minimum number of jumps=4

N=21
he will jump 1 step, he will reach (1,0)
he will jump 16 step, he will reach(17,0)
he will jump 4 step, he will reach(21,0)
so minimum number of jumps=3

Input :
First line will contain an integer T (number of test case).
Next T line will contain an integer N.

output :
For every input integer N, print the answer on a new line.

Time Limit : 1 Sec

Constraints :
0 ≤ N ≤ 10^18

Problem Setter:  Mohd Abdullah

SAMPLE INPUT
5
12
20
30
1000000000009
1

SAMPLE OUTPUT
2
2
4
15
1
"""

def minimum_jumps_to_library(N: int) -> int:
    """
    Calculate the minimum number of jumps required to reach the library located at (N,0) from (0,0).
    Beri can jump from (a,0) to (b,0) only if |b-a| can be expressed in the powers of 2.

    Parameters:
    N (int): The target coordinate on the x-axis where the library is located.

    Returns:
    int: The minimum number of jumps required.
    """
    ans = 0
    while N > 0:
        rem = N % 2
        if rem == 1:
            ans += 1
        N //= 2
    return ans