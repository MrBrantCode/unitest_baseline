"""
QUESTION:
Consider a directed graph whose vertices are numbered from 1 to n. There is an edge from a vertex i to a vertex j iff either j = i + 1 or j = 3 * i. The task is to find the minimum number of edges in a path in G from vertex 1 to vertex n.
Example 1:
Input:
N = 9
Output:
2
Explanation:
9 -> 3 -> 1, so
number of steps are 2. 
Ã¢â¬â¹Example 2:
Input:
N = 4
Output:
2
Explanation:
4 -> 3 -> 1, so
number of steps are 2.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minimumStep() which takes the N as inputs and returns the answer.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def minimum_steps_to_reach(n: int) -> int:
    """
    Calculate the minimum number of edges required to reach vertex `n` from vertex `1`
    in a directed graph where an edge exists from vertex `i` to vertex `j` iff either
    `j = i + 1` or `j = 3 * i`.

    Parameters:
    - n (int): The target vertex number.

    Returns:
    - int: The minimum number of edges (steps) required.
    """
    steps = 0
    while n != 1:
        if n % 3 == 0:
            n //= 3
        else:
            n -= 1
        steps += 1
    return steps