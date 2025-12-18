"""
QUESTION:
Write a function `cummulative_area(A, B, C, D, E, F, G, H)` that calculates the cumulative area encompassed by two orthogonal rectangles on a Cartesian plane. The rectangles are defined by their lower-left and upper-right vertices `(A, B)` and `(C, D)` for the first rectangle, and `(E, F)` and `(G, H)` for the second rectangle. The function should return the total area of the two rectangles, subtracting the area of their intersection if they intersect. The input values are restricted to `-104 <= A, B, C, D, E, F, G, H <= 104`.
"""

def cummulative_area(A, B, C, D, E, F, G, H):
    # Calculate the area of both rectangles
    area1 = (C - A) * (D - B)
    area2 = (G - E) * (H - F)

    # Calculate the overlapping area
    overlap_x = max(0, min(C, G) - max(A, E))
    overlap_y = max(0, min(D, H) - max(B, F))
    overlap_area = overlap_x * overlap_y

    # Calculate the total area
    total_area = area1 + area2 - overlap_area

    return total_area