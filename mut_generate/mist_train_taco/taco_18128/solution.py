"""
QUESTION:
A histogram is made of a number of contiguous bars, which have same width.

For a given histogram with $N$ bars which have a width of 1 and a height of $h_i$ = $h_1, h_2, ... , h_N$ respectively, find the area of the largest rectangular area.

Constraints

* $1 \leq N \leq 10^5$
* $0 \leq h_i \leq 10^9$

Input

The input is given in the following format.

$N$
$h_1$ $h_2$ ... $h_N$

Output

Print the area of the largest rectangle.

Examples

Input

8
2 1 3 5 3 4 2 1


Output

12


Input

3
2 0 1


Output

2
"""

def largest_rectangle_area(heights: list[int]) -> int:
    """
    Calculate the area of the largest rectangle in a histogram.

    Parameters:
    heights (list[int]): A list of integers representing the heights of the histogram bars.

    Returns:
    int: The area of the largest rectangle that can be formed in the histogram.
    """
    stk = []
    ans = 0
    N = len(heights)
    
    for i in range(N):
        if not stk:
            stk.append((heights[i], i))
        elif stk[-1][0] < heights[i]:
            stk.append((heights[i], i))
        elif stk[-1][0] == heights[i]:
            pass
        else:
            lastpos = None
            while stk and stk[-1][0] > heights[i]:
                nh, np = stk[-1]
                lastpos = np
                stk.pop()
                ans = max(ans, nh * (i - np))
            stk.append((heights[i], lastpos if lastpos is not None else i))
    
    # Process remaining elements in the stack
    while stk:
        nh, np = stk[-1]
        stk.pop()
        ans = max(ans, nh * (N - np))
    
    return ans