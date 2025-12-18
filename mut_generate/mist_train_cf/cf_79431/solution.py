"""
QUESTION:
Given a set of points and their corresponding Voronoi tessellation, and a set of additional points, write a function `locate_points(vor, extra)` that returns a numpy array of indices representing the Voronoi cell in which each extra point is located. The input `vor` is a scipy.spatial.Voronoi object and `extra` is a list of extra points. The function should return a numpy array where each element corresponds to the index of the Voronoi cell that contains the corresponding extra point.
"""

import numpy as np

def locate_points(vor, extra):
    points = vor.points
    point_region = vor.point_region

    locate_extra_points = []
    for extra_point in extra:
        min_index = np.argmin([np.linalg.norm(np.array(extra_point)-point) for point in points])
        locate_extra_points.append(point_region[min_index])

    return np.array(locate_extra_points)