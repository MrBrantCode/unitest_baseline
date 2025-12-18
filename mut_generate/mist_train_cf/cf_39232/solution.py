"""
QUESTION:
Implement a function `opposite_hemisphere_vertices(vertices, dist_thresh)` that identifies the vertices on the equator in a 3D space that are in the opposite hemisphere to any vertex in the input `vertices` based on a given distance threshold.

`vertices` is a list of tuples, each representing the coordinates of a vertex in the form `(x, y, z)`. `dist_thresh` is a float representing the maximum Euclidean distance for a vertex on the equator to be considered in the opposite hemisphere to another vertex. If `dist_thresh` is not provided, use a default threshold based on the input data type.

The function should return a list of indices of the vertices on the equator that are in the opposite hemisphere to any vertex in the input `vertices`.
"""

import numpy as np

def opposite_hemisphere_vertices(vertices, dist_thresh=None):
    equator_vertices = [v for v in vertices if v[2] == 0]  

    if dist_thresh is None:
        dist_thresh = np.finfo(float).eps  

    opposite_indices = []
    for i, v in enumerate(equator_vertices):
        opposite = False
        for v_dash in vertices:
            if v_dash[2] != 0:  
                continue
            if np.linalg.norm(np.array(v) * -1 - np.array(v_dash)) <= dist_thresh:
                opposite = True
                break
        if opposite:
            opposite_indices.append(vertices.index(v))

    return opposite_indices