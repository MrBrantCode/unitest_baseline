"""
QUESTION:
Given a matrix (H × W) which contains only 1 and 0, find the area of the largest rectangle which only contains 0s.

Constraints

* 1 ≤ H, W ≤ 1,400

Input


H W
c1,1 c1,2 ... c1,W
c2,1 c2,2 ... c2,W
:
cH,1 cH,2 ... cH,W


In the first line, two integers H and W separated by a space character are given. In the following H lines, ci,j, elements of the H × W matrix, are given.

Output

Print the area (the number of 0s) of the largest rectangle.

Example

Input

4 5
0 0 1 0 0
1 0 0 0 0
0 0 0 1 0
0 0 0 1 0


Output

6
"""

def largest_rectangle_of_zeros(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    H = len(matrix)
    W = len(matrix[0])
    height = [0] * W
    max_area = 0
    
    for row in matrix:
        height = [0 if t else height[j] + 1 for j, t in enumerate(row)]
        height.append(0)
        stack = []
        
        for i, h in enumerate(height):
            if stack:
                if stack[-1][1] == h:
                    continue
                elif stack[-1][1] > h:
                    while stack and stack[-1][1] >= h:
                        i_stack, h_stack = stack.pop()
                        max_area = max(max_area, (i - i_stack) * h_stack)
                    i = i_stack
            stack.append((i, h))
    
    return max_area