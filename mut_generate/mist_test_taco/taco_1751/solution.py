"""
QUESTION:
Cowboy Vlad has a birthday today! There are $n$ children who came to the celebration. In order to greet Vlad, the children decided to form a circle around him. Among the children who came, there are both tall and low, so if they stand in a circle arbitrarily, it may turn out, that there is a tall and low child standing next to each other, and it will be difficult for them to hold hands. Therefore, children want to stand in a circle so that the maximum difference between the growth of two neighboring children would be minimal possible.

Formally, let's number children from $1$ to $n$ in a circle order, that is, for every $i$ child with number $i$ will stand next to the child with number $i+1$, also the child with number $1$ stands next to the child with number $n$. Then we will call the discomfort of the circle the maximum absolute difference of heights of the children, who stand next to each other.

Please help children to find out how they should reorder themselves, so that the resulting discomfort is smallest possible.


-----Input-----

The first line contains a single integer $n$ ($2 \leq n \leq 100$) — the number of the children who came to the cowboy Vlad's birthday.

The second line contains integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 10^9$) denoting heights of every child.


-----Output-----

Print exactly $n$ integers — heights of the children in the order in which they should stand in a circle. You can start printing a circle with any child.

If there are multiple possible answers, print any of them.


-----Examples-----
Input
5
2 1 1 3 2

Output
1 2 3 2 1

Input
3
30 10 20

Output
10 20 30



-----Note-----

In the first example, the discomfort of the circle is equal to $1$, since the corresponding absolute differences are $1$, $1$, $1$ and $0$. Note, that sequences $[2, 3, 2, 1, 1]$ and $[3, 2, 1, 1, 2]$ form the same circles and differ only by the selection of the starting point.

In the second example, the discomfort of the circle is equal to $20$, since the absolute difference of $10$ and $30$ is equal to $20$.
"""

def minimize_discomfort(n, heights):
    # Sort the heights to facilitate the arrangement
    heights.sort()
    
    # Initialize the result list with -1 to indicate unassigned positions
    result = [-1] * n
    
    # Calculate the middle index
    middle = n // 2
    
    # Place the largest height in the middle of the result list
    result[middle] = heights[-1]
    
    # Initialize indices for placing the remaining heights
    left = middle - 1
    right = middle + 1
    index = n - 2
    
    # Fill the result list with heights in a way that minimizes discomfort
    while left >= 0 and right < n:
        result[left] = heights[index]
        index -= 1
        left -= 1
        
        if index >= 0:
            result[right] = heights[index]
            index -= 1
            right += 1
    
    # If there's an odd number of children, the loop above will handle it
    # If there's an even number of children, we need to place the smallest height at the start
    if n % 2 == 0:
        result[0] = heights[0]
    
    return result