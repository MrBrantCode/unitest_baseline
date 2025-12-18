"""
QUESTION:
There are 2N squares arranged from left to right. You are given a string of length 2N representing the color of each of the squares.

The color of the i-th square from the left is black if the i-th character of S is `B`, and white if that character is `W`.

You will perform the following operation exactly N times: choose two distinct squares, then invert the colors of these squares and the squares between them. Here, to invert the color of a square is to make it white if it is black, and vice versa.

Throughout this process, you cannot choose the same square twice or more. That is, each square has to be chosen exactly once.

Find the number of ways to make all the squares white at the end of the process, modulo 10^9+7.

Two ways to make the squares white are considered different if and only if there exists i (1 \leq i \leq N) such that the pair of the squares chosen in the i-th operation is different.

Constraints

* 1 \leq N \leq 10^5
* |S| = 2N
* Each character of S is `B` or `W`.

Input

Input is given from Standard Input in the following format:


N
S


Output

Print the number of ways to make all the squares white at the end of the process, modulo 10^9+7. If there are no such ways, print 0.

Examples

Input

2
BWWB


Output

4


Input

4
BWBBWWWB


Output

288


Input

5
WWWWWWWWWW


Output

0
"""

from math import factorial

def count_ways_to_make_squares_white(N, S):
    mod = 10 ** 9 + 7
    
    # Early exit if the first or last square is white
    if S[0] == 'W' or S[-1] == 'W':
        return 0
    
    # Initialize the array to track the parity of the operations
    arr = ['L']
    swap_dict = {'L': 'R', 'R': 'L'}
    
    # Fill the array based on the parity of the operations
    for i in range(1, 2 * N):
        arr.append(arr[i - 1] if S[i] != S[i - 1] else swap_dict[arr[i - 1]])
    
    # Check if the number of 'L' and 'R' operations are balanced
    if arr.count('L') != arr.count('R'):
        return 0
    
    # Calculate the number of ways to perform the operations
    cnt_tmp = 0
    cnt_swap = 1
    for a in arr:
        if a == 'L':
            cnt_tmp += 1
        else:
            cnt_swap = cnt_swap * cnt_tmp % mod
            cnt_tmp -= 1
    
    # Return the result modulo 10^9 + 7
    return cnt_swap * factorial(N) % mod