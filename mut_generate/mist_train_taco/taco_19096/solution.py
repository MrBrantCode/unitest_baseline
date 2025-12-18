"""
QUESTION:
Ilya lives in a beautiful city of Chordalsk.

There are $n$ houses on the street Ilya lives, they are numerated from $1$ to $n$ from left to right; the distance between every two neighboring houses is equal to $1$ unit. The neighboring houses are $1$ and $2$, $2$ and $3$, ..., $n-1$ and $n$. The houses $n$ and $1$ are not neighboring.

The houses are colored in colors $c_1, c_2, \ldots, c_n$ so that the $i$-th house is colored in the color $c_i$. Everyone knows that Chordalsk is not boring, so there are at least two houses colored in different colors.

Ilya wants to select two houses $i$ and $j$ so that $1 \leq i < j \leq n$, and they have different colors: $c_i \neq c_j$. He will then walk from the house $i$ to the house $j$ the distance of $(j-i)$ units.

Ilya loves long walks, so he wants to choose the houses so that the distance between them is the maximum possible.

Help Ilya, find this maximum possible distance.


-----Input-----

The first line contains a single integer $n$ ($3 \leq n \leq 300\,000$) — the number of cities on the street.

The second line contains $n$ integers $c_1, c_2, \ldots, c_n$ ($1 \leq c_i \leq n$) — the colors of the houses.

It is guaranteed that there is at least one pair of indices $i$ and $j$ so that $1 \leq i < j \leq n$ and $c_i \neq c_j$.


-----Output-----

Print a single integer — the maximum possible distance Ilya can walk.


-----Examples-----
Input
5
1 2 3 2 3

Output
4

Input
3
1 2 1

Output
1

Input
7
1 1 3 1 1 1 1

Output
4



-----Note-----

In the first example the optimal way is to walk from the first house to the last one, where Ilya can walk the distance of $5-1 = 4$ units.

In the second example the optimal way is to either walk from the first house to the second or from the second to the third. Both these ways have the distance of $1$ unit.

In the third example the optimal way is to walk from the third house to the last one, where Ilya can walk the distance of $7-3 = 4$ units.
"""

def max_walk_distance(n, colors):
    l1 = colors[0]
    l2 = None
    l2p = 0
    
    # Find the first house with a different color from the first house
    for i in range(n):
        if colors[i] != l1:
            l2 = colors[i]
            l2p = i
            break
    
    r1 = colors[-1]
    r2 = None
    r2p = 0
    
    # Find the last house with a different color from the last house
    for i in range(n - 1, -1, -1):
        if colors[i] != r1:
            r2 = colors[i]
            r2p = i
            break
    
    # If the first and last houses have different colors, the max distance is n-1
    if l1 != r1:
        return n - 1
    else:
        # Otherwise, return the maximum distance between the first different color
        # from the left and the first different color from the right
        return max(r2p, n - 1 - l2p)