"""
QUESTION:
A tatami mat, a Japanese traditional floor cover, has a rectangular form with aspect ratio 1:2. When spreading tatami mats on a floor, it is prohibited to make a cross with the border of the tatami mats, because it is believed to bring bad luck.

Your task is to write a program that reports how many possible ways to spread tatami mats of the same size on a floor of given height and width.



Input

The input consists of multiple datasets. Each dataset cosists of a line which contains two integers H and W in this order, separated with a single space. H and W are the height and the width of the floor respectively. The length of the shorter edge of a tatami mat is regarded as a unit length.

You may assume 0 < H, W ≤ 20.

The last dataset is followed by a line containing two zeros. This line is not a part of any dataset and should not be processed.

Output

For each dataset, print the number of possible ways to spread tatami mats in one line.

Example

Input

3 4
4 4
0 0


Output

4
2
"""

def count_tatami_arrangements(H: int, W: int) -> int:
    """
    Counts the number of possible ways to spread tatami mats on a floor of given height and width.

    Parameters:
    H (int): The height of the floor.
    W (int): The width of the floor.

    Returns:
    int: The number of possible ways to spread the tatami mats.
    """
    if H * W % 2 == 1:
        return 0
    
    state = [[-1] * W for _ in range(H)]
    
    def dfs(k: int) -> int:
        if k == H * W:
            return 1
        i, j = divmod(k, W)
        if state[i][j] != -1:
            return dfs(k + 1)
        if i > 0 and j > 0 and (state[i - 1][j - 1] != state[i - 1][j] != state[i][j - 1] != state[i - 1][j - 1]):
            return 0
        r = 0
        state[i][j] = k
        if i + 1 < H:
            state[i + 1][j] = k
            r += dfs(k + 1)
            state[i + 1][j] = -1
        if j + 1 < W and state[i][j + 1] == -1:
            state[i][j + 1] = k
            r += dfs(k + 1)
            state[i][j + 1] = -1
        state[i][j] = -1
        return r
    
    return dfs(0)