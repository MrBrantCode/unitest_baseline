"""
QUESTION:
Implement the function `calculate_total_bar_area(data)` that takes a 4-dimensional numpy array `data` as input, representing bar chart data. Each bar is defined by four coordinates: x1, y1, x2, y2. The function should calculate the total area covered by the bars in the chart, where the area of each bar is (x2 - x1) * (y2 - y1). The input array `data` has the following structure: data[group index, bar index, corner index (0 for x-coordinate, 1 for y-coordinate), coordinate value]. The function should return the total area covered by all the bars.
"""

import numpy as np

def calculate_total_bar_area(data):
    areas = np.prod(data[:, :, 1, :] - data[:, :, 0, :], axis=2)
    total_area = np.sum(areas)
    return total_area