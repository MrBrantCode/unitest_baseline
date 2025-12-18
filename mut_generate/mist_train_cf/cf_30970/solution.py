"""
QUESTION:
Implement the `_distance_deviation` method of the `HandwritingRecognition` class. The method takes a list of strokes as input, where each stroke object has a `horizontal_distance` method that calculates the horizontal distance between the current stroke and another stroke. The method should return the standard deviation of the horizontal distances between consecutive strokes in the input list. The class has an attribute `_source` which is not used in this method. The input list of strokes is guaranteed to have at least two strokes.
"""

import numpy as np

def distance_deviation(strokes):
    delayed_strokes = strokes[1:]

    distances = []
    for i in range(len(delayed_strokes)):
        next_stroke = delayed_strokes[i]
        stroke = strokes[i]
        distances.append(next_stroke.horizontal_distance(stroke))

    return np.std(distances)