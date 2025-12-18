"""
QUESTION:
Vasya has a beautiful garden where wonderful fruit trees grow and yield fantastic harvest every year. But lately thieves started to sneak into the garden at nights and steal the fruit too often. Vasya can’t spend the nights in the garden and guard the fruit because there’s no house in the garden! Vasya had been saving in for some time and finally he decided to build the house. The rest is simple: he should choose in which part of the garden to build the house. In the evening he sat at his table and drew the garden’s plan. On the plan the garden is represented as a rectangular checkered field n × m in size divided into squares whose side length is 1. In some squares Vasya marked the trees growing there (one shouldn’t plant the trees too close to each other that’s why one square contains no more than one tree). Vasya wants to find a rectangular land lot a × b squares in size to build a house on, at that the land lot border should go along the lines of the grid that separates the squares. All the trees that grow on the building lot will have to be chopped off. Vasya loves his garden very much, so help him choose the building land lot location so that the number of chopped trees would be as little as possible.

Input

The first line contains two integers n and m (1 ≤ n, m ≤ 50) which represent the garden location. The next n lines contain m numbers 0 or 1, which describe the garden on the scheme. The zero means that a tree doesn’t grow on this square and the 1 means that there is a growing tree. The last line contains two integers a and b (1 ≤ a, b ≤ 50). Note that Vasya can choose for building an a × b rectangle as well a b × a one, i.e. the side of the lot with the length of a can be located as parallel to the garden side with the length of n, as well as parallel to the garden side with the length of m.

Output

Print the minimum number of trees that needs to be chopped off to select a land lot a × b in size to build a house on. It is guaranteed that at least one lot location can always be found, i. e. either a ≤ n and b ≤ m, or a ≤ m и b ≤ n.

Examples

Input

2 2
1 0
1 1
1 1


Output

0


Input

4 5
0 0 1 0 1
0 1 1 1 0
1 0 1 0 1
1 1 1 1 1
2 3


Output

2

Note

In the second example the upper left square is (1,1) and the lower right is (3,2).
"""

def min_trees_to_chop(n, m, garden, a, b):
    # Create a prefix sum array for the garden
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = garden[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    
    def count_trees(x1, y1, x2, y2):
        return prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    
    min_trees = float('inf')
    
    # Check for a x b rectangle
    if a <= n and b <= m:
        for i in range(1, n - a + 2):
            for j in range(1, m - b + 2):
                min_trees = min(min_trees, count_trees(i, j, i + a - 1, j + b - 1))
    
    # Check for b x a rectangle
    if b <= n and a <= m:
        for i in range(1, n - b + 2):
            for j in range(1, m - a + 2):
                min_trees = min(min_trees, count_trees(i, j, i + b - 1, j + a - 1))
    
    return min_trees