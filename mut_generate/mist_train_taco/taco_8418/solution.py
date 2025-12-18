"""
QUESTION:
You've got a rectangular parallelepiped with integer edge lengths. You know the areas of its three faces that have a common vertex. Your task is to find the sum of lengths of all 12 edges of this parallelepiped.

Input

The first and the single line contains three space-separated integers — the areas of the parallelepiped's faces. The area's values are positive ( > 0) and do not exceed 104. It is guaranteed that there exists at least one parallelepiped that satisfies the problem statement.

Output

Print a single number — the sum of all edges of the parallelepiped.

Examples

Input

1 1 1


Output

12


Input

4 6 6


Output

28

Note

In the first sample the parallelepiped has sizes 1 × 1 × 1, in the second one — 2 × 2 × 3.
"""

def calculate_edge_sum(face_area_1: int, face_area_2: int, face_area_3: int) -> int:
    """
    Calculate the sum of all 12 edges of a rectangular parallelepiped given the areas of its three faces.

    Parameters:
    - face_area_1 (int): The area of the first face.
    - face_area_2 (int): The area of the second face.
    - face_area_3 (int): The area of the third face.

    Returns:
    - int: The sum of all 12 edges of the parallelepiped.
    """
    import math
    
    # Calculate the lengths of the edges
    a = math.sqrt((face_area_1 * face_area_3) / face_area_2)
    b = math.sqrt((face_area_1 * face_area_2) / face_area_3)
    c = math.sqrt((face_area_2 * face_area_3) / face_area_1)
    
    # Sum of all edges
    edge_sum = 4 * (a + b + c)
    
    return int(edge_sum)