"""
QUESTION:
Implement a function `count_unique_objects(detections, threshold)` that takes a list of tuples `detections` representing x and y coordinates of detected objects and a float `threshold` representing the maximum distance for two detections to be considered the same object. Return the count of unique objects detected within the given threshold.
"""

import math

def count_unique_objects(detections, threshold):
    unique_objects = set()
    
    for i in range(len(detections)):
        for j in range(i+1, len(detections)):
            distance = math.sqrt((detections[i][0] - detections[j][0])**2 + (detections[i][1] - detections[j][1])**2)
            if distance <= threshold:
                unique_objects.add(detections[i])
                unique_objects.add(detections[j])
    
    return len(unique_objects)