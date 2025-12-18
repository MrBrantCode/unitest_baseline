"""
QUESTION:
Write a function named `minimumTotal` that takes a 2D list `triangle` as input. The function should return the smallest path sum from the apex to the base of the triangle, where in each progression, you can transition to a number that is adjacent in the subsequent row. The function should use O(n) additional space, where `n` is the total number of rows in the triangle. The input `triangle` satisfies the following restrictions: `1 <= triangle.length <= 200`, `triangle[0].length == 1`, `triangle[i].length == triangle[i - 1].length + 1`, and `-10^4 <= triangle[i][j] <= 10^4`.
"""

def minimumTotal(triangle):
    if not triangle:
        return 
    res = triangle[-1]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    return res[0]