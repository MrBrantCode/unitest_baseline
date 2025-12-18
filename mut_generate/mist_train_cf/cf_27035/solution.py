"""
QUESTION:
Write a function `calculateTotalArea(rectangles)` that takes a list of rectangles as input, where each rectangle is represented by a tuple `(x1, y1, x2, y2)` denoting the bottom-left and top-right coordinates. The function should return the total area covered by the rectangles, excluding any overlapping regions.
"""

def calculateTotalArea(rectangles):
    def area(x1, y1, x2, y2):
        return (x2 - x1) * (y2 - y1)

    total_area = 0
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        total_area += area(x1, y1, x2, y2)

    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            x_overlap = max(0, min(rectangles[i][2], rectangles[j][2]) - max(rectangles[i][0], rectangles[j][0]))
            y_overlap = max(0, min(rectangles[i][3], rectangles[j][3]) - max(rectangles[i][1], rectangles[j][1]))
            overlap_area = x_overlap * y_overlap
            total_area -= overlap_area

    return total_area