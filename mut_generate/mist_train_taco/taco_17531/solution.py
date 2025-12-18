"""
QUESTION:
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle


[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

def minimum_path_sum(triangle):
    length = len(triangle)
    for i in range(length - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
    return triangle[0][0]