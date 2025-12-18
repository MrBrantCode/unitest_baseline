"""
QUESTION:
You are given N unit squares (squares with side length 1 unit), the task is to make rectangles using these squares and to count the number of rotationally unique rectangles. Two rectangles are rotationally unique if one can’t be rotated to become equivalent to the other one.
 
Example 1:
Input:
N = 4
Output:
5
Explanation:
Total rectangles we can make from 4
unit squares are: 1x1, 1x2, 1x3, 2x2,
1x4, 2x1, 3x1, and 4x1.
But we can get 2x1, 3x1, 4x1
by rotating 1x2, 1x3, 1x4.
So these five rectangles are rotationally unique.
1x1, 1x2, 2x2, 1x3 and 1x4.
Example 2:
Input:
N = 5
Output:
6
Explanation:
We can make only 6 rotationally unique
rectangles from 5 unit squares.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfUniqueRectangles() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(N*sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

def count_rotationally_unique_rectangles(N: int) -> int:
    count = 0
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if i * j <= N:
                count += 1
            else:
                break
    return count