"""
QUESTION:
In some other world, today is Christmas.
Mr. Takaha decides to make a multi-dimensional burger in his party. A level-L burger (L is an integer greater than or equal to 0) is the following thing:
 - A level-0 burger is a patty.
 - A level-L burger (L \geq 1) is a bun, a level-(L-1) burger, a patty, another level-(L-1) burger and another bun, stacked vertically in this order from the bottom.
For example, a level-1 burger and a level-2 burger look like BPPPB and BBPPPBPBPPPBB (rotated 90 degrees), where B and P stands for a bun and a patty.
The burger Mr. Takaha will make is a level-N burger. Lunlun the Dachshund will eat X layers from the bottom of this burger (a layer is a patty or a bun). How many patties will she eat?

-----Constraints-----
 - 1 \leq N \leq 50
 - 1 \leq X \leq ( the total number of layers in a level-N burger )
 - N and X are integers.

-----Input-----
Input is given from Standard Input in the following format:
N X

-----Output-----
Print the number of patties in the bottom-most X layers from the bottom of a level-N burger.

-----Sample Input-----
2 7

-----Sample Output-----
4

There are 4 patties in the bottom-most 7 layers of a level-2 burger (BBPPPBPBPPPBB).
"""

def count_patties_eaten(N, X):
    # Precompute the number of layers and patties for each level
    a = [1]  # a[i] is the total number of layers in a level-i burger
    p = [1]  # p[i] is the total number of patties in a level-i burger
    
    for i in range(N):
        a.append(a[i] * 2 + 3)
        p.append(p[i] * 2 + 1)
    
    # Helper function to recursively count the patties
    def dfs(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + a[n - 1]:
            return dfs(n - 1, x - 1)
        else:
            return p[n - 1] + 1 + dfs(n - 1, x - 2 - a[n - 1])
    
    # Return the result of the recursive function
    return dfs(N, X)