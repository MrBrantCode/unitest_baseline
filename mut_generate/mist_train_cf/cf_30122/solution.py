"""
QUESTION:
Design a function `detect_conflicts(line_segments, routingStrategy, edgeSpacing, conflictThreshold, createdJunctionPoints)` that takes in a list of horizontal line segments and system parameters to detect conflicts between overlapping line segments within a specified threshold. Each line segment is represented as a tuple of three integers (x1, y, x2) where (x1, y) and (x2, y) are the coordinates of the endpoints of the line segment. The function should return the total penalty for all detected conflicts, where the conflict penalty for overlapping line segments is defined as 16.
"""

def entance(line_segments, routingStrategy, edgeSpacing, conflictThreshold, createdJunctionPoints):
    CONFLICT_PENALTY = 16
    total_penalty = 0
    for i in range(len(line_segments)):
        for j in range(i+1, len(line_segments)):
            seg1 = line_segments[i]
            seg2 = line_segments[j]
            if seg1[1] == seg2[1]:  
                min_x = min(seg1[0], seg2[0])
                max_x = max(seg1[2], seg2[2])
                if max_x - min_x < conflictThreshold:  
                    total_penalty += CONFLICT_PENALTY
    return total_penalty