"""
QUESTION:
You have 4 types of lego blocks, of sizes (1 x 1 x 1), (1 x 1 x 2), (1 x 1 x 3), and (1 x 1 x 4). Assume that you have an infinite number of blocks of each type.

Using these blocks, you want to make a wall of height N and width M. The wall should not have any holes in it. The wall you build should be one solid structure. A solid structure can be interpreted in one of the following ways:
(1)It should not be possible to separate the wall along any vertical line without cutting any lego block used to build the wall.
(2)You cannot make a vertical cut from top to bottom without cutting one or more lego blocks.

The blocks can only be placed horizontally. In how many ways can the wall be built?

Input:

The first line contains the number of test cases T. T test cases follow. Each case contains two integers N and M.

Output:

Output T lines, one for each test case containing the number of ways to build the wall. As the numbers can be very large, output the result modulo 1000000007.

Constraints:

1 ≤ T ≤ 100
1 ≤ N,M ≤ 1000

SAMPLE INPUT
4
2 2
3 2
2 3
4 4

SAMPLE OUTPUT
3
7
9
3375

Explanation

For the first case, we can have

two (1 * 1 * 2) lego blocks stacked one on top of another.
one (1 * 1 * 2) block stacked on top of two (1 * 1 * 1) blocks.
two (1 * 1 * 1) blocks stacked on top of one (1 * 1 * 2) block.

For the second case, each row of the wall can contain either two blocks of width 1, or one block of width 2. However, the wall where all rows contain two blocks of width 1 is not a solid one as it can be divided vertically. Thus, the number of ways is 2 * 2 * 2 - 1 = 7.
"""

MOD = int(1e9+7)

def count_solid_wall_ways(N, M):
    # Initialize ways array to store the number of ways to build a row of width i
    ways = [0] * (M + 4)
    ways[0] = 1
    
    # Calculate the number of ways to build a row of width i using blocks of size 1, 2, 3, and 4
    for i in range(M):
        for j in range(1, 5):
            ways[i + j] = (ways[i + j] + ways[i]) % MOD
    
    # Initialize arrays to store the number of ways to build a wall of width i
    res = [0] * (M + 1)
    resbad = [0] * (M + 1)
    resgood = [0] * (M + 1)
    
    # Base case: there is only one way to build a wall of width 1
    resgood[1] = 1
    resbad[1] = 0
    res[1] = 1
    
    # Calculate the number of ways to build a wall of width i
    for i in range(2, M + 1):
        res[i] = pow(ways[i], N, MOD)
        for j in range(1, i):
            resbad[i] += (resgood[j] * res[i - j]) % MOD
        resgood[i] = (res[i] - resbad[i] % MOD + MOD) % MOD
    
    # Return the number of ways to build a solid wall of width M
    return resgood[M]