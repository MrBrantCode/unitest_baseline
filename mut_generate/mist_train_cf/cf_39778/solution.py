"""
QUESTION:
Implement the `check_line_intersects_triangles` function to determine whether a line segment intersects two different triangles defined by points in 3D space. The function should take as input the coordinates of the vertices of two triangles (`triangle1_points` and `triangle2_points`) and the coordinates of the endpoints of the line segment (`hand_end_pos` and `elbow_end_pos`). The function should return a boolean value indicating whether the line segment intersects both triangles.

The `line_intersects_triangle` method, which determines whether a line intersects a triangle in 3D space, is available for use. This method takes the coordinates of the triangle vertices and the endpoints of the line segment as input and returns a boolean value indicating whether the line intersects the triangle.

The function signature is:
```python
def check_line_intersects_triangles(triangle1_points, triangle2_points, hand_end_pos, elbow_end_pos):
    # Your implementation here
    pass
```
"""

def check_line_intersects_triangles(triangle1_points, triangle2_points, hand_end_pos, elbow_end_pos):
    def line_intersects_triangle(p1, p2, p3, p4, p5):
        v0 = p3 - p1
        v1 = p2 - p1
        v2 = p4 - p1

        dot00 = np.dot(v0, v0)
        dot01 = np.dot(v0, v1)
        dot02 = np.dot(v0, v2)
        dot11 = np.dot(v1, v1)
        dot12 = np.dot(v1, v2)

        inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom

        if (u >= 0) and (v >= 0) and (u + v < 1):
            t = (np.dot(v2, v2) - dot02 * u - dot12 * v) * inv_denom
            if t > 0:
                return True
        return False

    forearm_intersects_triangle1 = line_intersects_triangle(triangle1_points[0], triangle1_points[1], triangle1_points[2], hand_end_pos, elbow_end_pos)
    forearm_intersects_triangle2 = line_intersects_triangle(triangle2_points[0], triangle2_points[1], triangle2_points[2], hand_end_pos, elbow_end_pos)

    return forearm_intersects_triangle1 and forearm_intersects_triangle2