"""
QUESTION:
There are N blocks arranged in a row. Let us paint these blocks.
We will consider two ways to paint the blocks different if and only if there is a block painted in different colors in those two ways.
Find the number of ways to paint the blocks under the following conditions:
 - For each block, use one of the M colors, Color 1 through Color M, to paint it. It is not mandatory to use all the colors.
 - There may be at most K pairs of adjacent blocks that are painted in the same color.
Since the count may be enormous, print it modulo 998244353.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N, M \leq 2 \times 10^5
 - 0 \leq K \leq N - 1

-----Input-----
Input is given from Standard Input in the following format:
N M K

-----Output-----
Print the answer.

-----Sample Input-----
3 2 1

-----Sample Output-----
6

The following ways to paint the blocks satisfy the conditions: 112, 121, 122, 211, 212, and 221. Here, digits represent the colors of the blocks.
"""

def count_painting_ways(N: int, M: int, K: int, mod: int = 998244353) -> int:
    """
    Calculate the number of ways to paint N blocks using M colors such that at most K pairs of adjacent blocks
    are painted in the same color, modulo 998244353.

    Parameters:
    - N (int): The number of blocks.
    - M (int): The number of colors available.
    - K (int): The maximum number of pairs of adjacent blocks that can be painted in the same color.
    - mod (int): The modulo value (default is 998244353).

    Returns:
    - int: The number of ways to paint the blocks modulo mod.
    """
    # Precompute factorials and their modular inverses
    f = 1
    f_list = [1]
    for m in range(1, N + 1):
        f *= m
        f %= mod
        f_list.append(f)
    
    inv = pow(f, mod - 2, mod)
    inv_list = [1] * (N + 1)
    inv_list[N] = inv
    for m in range(N, 1, -1):
        inv *= m
        inv %= mod
        inv_list[m - 1] = inv
    
    # Calculate the number of ways to paint the blocks
    ans = 0
    for i in range(K + 1):
        color = pow(M - 1, N - 1 - i, mod)
        order = f_list[N - 1] * inv_list[i] * inv_list[N - i - 1] % mod
        ans += color * order * M % mod
        ans = ans % mod
    
    return ans