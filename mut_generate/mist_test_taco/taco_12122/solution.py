"""
QUESTION:
Chef has  $N$ doggo (dogs) , Lets number them $1$ to $N$.

Chef decided to build houses for each, but he soon realizes that keeping so many dogs at one place may be messy. So he decided to divide them into several groups called doggo communities. Let the total no. of groups be $K$ . In a community, paths between pairs of houses can be made so that doggo can play with each other. But there cannot be a path between two houses of different communities for sure. Chef wanted to make maximum no. of paths such that the total path is not greater then $K$.
Let’s visualize this problem in an engineer's way :)
The problem is to design a graph with max edge possible such that the total no. of edges should not be greater than the total no. of connected components.

-----INPUT FORMAT-----
- First line of each test case file contain $T$ , denoting total number of test cases.
- $ith$ test case contain only one line with a single integer $N$ , denoting the number of dogs(vertex)

-----OUTPUT FORMAT-----
- For each test case print a line with a integer , denoting the maximum possible path possible.

-----Constraints-----
- $1 \leq T \leq 10000$
- $1 \leq N \leq 10^9$ 

-----Sub-Tasks-----
- $20 Points$
- $1 \leq N \leq 10^6$ 

-----Sample Input-----
1

4

-----Sample Output-----
2

-----Explanation-----
4 houses can be made with  like this:

community #1  : [1 - 2  ]

community #2 :  [3 - 4 ]

or  [1 - 2 - 3]  , [ 4 ]

In both cases the maximum possible path is 2.
"""

import math

def calculate_max_paths(n):
    """
    Calculate the maximum possible paths in a graph with n vertices such that the total number of edges
    does not exceed the total number of connected components.

    Parameters:
    n (int): The number of vertices (dogs).

    Returns:
    int: The maximum possible paths.
    """
    a = 1
    b = 1
    c = -2 * n
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    r1 = (-b + sqrt_val) / (2 * a)
    r1 = math.floor(r1) + 1
    return n - r1 + 1