"""
QUESTION:
Implement a function `extract_target_polygon(bbox, polygons)` that takes a bounding box `bbox` and a list of polygons `polygons` as input and returns the first polygon that lies completely within the given bounding box. The bounding box is represented as a tuple `(min_x, min_y, max_x, max_y)`, and each polygon is a list of vertices, where each vertex is a tuple `(x, y)`. If no polygon lies within the bounding box, return `None`.
"""

def extract_target_polygon(bbox, polygons):
    min_x, min_y, max_x, max_y = bbox
    for polygon in polygons:
        x_coords = [vertex[0] for vertex in polygon]
        y_coords = [vertex[1] for vertex in polygon]
        if all(min_x <= x <= max_x and min_y <= y <= max_y for x, y in polygon):
            return polygon
    return None