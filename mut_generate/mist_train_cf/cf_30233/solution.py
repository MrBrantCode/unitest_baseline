"""
QUESTION:
Implement the `largestRectangleArea` function, which takes a binary matrix as input and returns the area of the largest rectangle of 1s within the matrix. The matrix consists of 0s and 1s, where 1 represents a filled cell and 0 represents an empty cell. The function should only return the maximum area, not the coordinates or shape of the rectangle.
"""

def largestRectangleArea(matrix):
    def largestRectangleAreaHistogram(heights):
        stack = []
        max_area = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)
        while stack:
            top = stack.pop()
            width = i if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
        return max_area

    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0

    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == 1 else 0
        max_area = max(max_area, largestRectangleAreaHistogram(heights))

    return max_area