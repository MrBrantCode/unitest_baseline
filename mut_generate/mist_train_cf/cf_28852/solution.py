"""
QUESTION:
Implement a function `polygon_triangulation(vertices)` that takes a list of vertices representing a simple polygon in counterclockwise order and returns a list of triangles that partition the polygon into non-overlapping triangles. The function should use a stack data structure to triangulate the polygon, ensuring that the resulting triangles do not overlap.
"""

def polygon_triangulation(vertices):
    def is_convex(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) >= 0

    stack = []
    triangles = []

    for idx, v in enumerate(vertices):
        while len(stack) > 1 and not is_convex(vertices[stack[-2]], vertices[stack[-1]], v):
            top = stack.pop()
            triangles.append((vertices[stack[-1]], vertices[top], v))
        stack.append(idx)

    while len(stack) > 2:
        top = stack.pop()
        triangles.append((vertices[stack[-1]], vertices[top], vertices[stack[0]]))

    return triangles