"""
QUESTION:
During her tantrums the princess usually smashes some collectable porcelain. Every furious shriek is accompanied with one item smashed.

The collection of porcelain is arranged neatly on n shelves. Within each shelf the items are placed in one row, so that one can access only the outermost items — the leftmost or the rightmost item, not the ones in the middle of the shelf. Once an item is taken, the next item on that side of the shelf can be accessed (see example). Once an item is taken, it can't be returned to the shelves.

You are given the values of all items. Your task is to find the maximal damage the princess' tantrum of m shrieks can inflict on the collection of porcelain.

Input

The first line of input data contains two integers n (1 ≤ n ≤ 100) and m (1 ≤ m ≤ 10000). The next n lines contain the values of the items on the shelves: the first number gives the number of items on this shelf (an integer between 1 and 100, inclusive), followed by the values of the items (integers between 1 and 100, inclusive), in the order in which they appear on the shelf (the first number corresponds to the leftmost item, the last one — to the rightmost one). The total number of items is guaranteed to be at least m.

Output

Output the maximal total value of a tantrum of m shrieks.

Examples

Input

2 3
3 3 7 2
3 4 1 5


Output

15


Input

1 3
4 4 3 1 2


Output

9

Note

In the first case there are two shelves, each with three items. To maximize the total value of the items chosen, one can take two items from the left side of the first shelf and one item from the right side of the second shelf.

In the second case there is only one shelf, so all three items are taken from it — two from the left side and one from the right side.
"""

def maximal_damage(n, m, shelves):
    # Initialize a list to store the maximum values for each shelf
    _dp = [[] for _ in range(n)]
    
    # Process each shelf
    for i in range(n):
        ni = len(shelves[i])
        ai = shelves[i]
        cumsum = [0] * (ni + 1)
        
        # Calculate cumulative sums for the current shelf
        for j in range(ni):
            cumsum[j + 1] = cumsum[j] + ai[j]
        
        _dpi = [0] * (ni + 1)
        
        # Calculate the maximum values for the current shelf
        for j in range(ni + 1):
            for k in range(j, ni + 1):
                _dpi[ni + j - k] = max(_dpi[ni + j - k], cumsum[j] + cumsum[-1] - cumsum[k])
        
        _dp[i] = _dpi
    
    # Initialize the dp array for the final result
    dp = [0] * (m + 1)
    
    # Calculate the final maximal damage
    for i in range(n):
        _dpi = _dp[i]
        for j in reversed(range(m + 1)):
            dpj = dp[j]
            for k in range(min(len(_dp[i]), j + 1)):
                dpj = max(dpj, _dpi[k] + dp[j - k])
            dp[j] = dpj
    
    return dp[m]