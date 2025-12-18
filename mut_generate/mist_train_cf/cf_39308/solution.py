"""
QUESTION:
Write a function `process_anomaly_segments(pred, anomaly_segments, L)` that takes in the following parameters:
- `pred`: A list of integers representing the center locations.
- `anomaly_segments`: A list of lists, where each inner list represents a segment with two integers denoting the start and end points.
- `L`: An integer representing the range.

The function should return a tuple containing two values:
1. The count of correct anomaly segments.
2. The ratio of correct anomaly segments to the total number of anomaly segments.

The function must calculate the center location `P` as the middle value of `pred`, and then check if `P` falls within a specific range for each segment in `anomaly_segments`. The range for each segment is from `seg[0] - L` to `seg[-1] + L`. If `P` falls within the range, it increments the count of correct anomaly segments. The function should return the count of correct segments and the ratio of correct segments to the total number of anomaly segments.
"""

def process_anomaly_segments(pred, anomaly_segments, L):
    correct = 0  
    for seg in anomaly_segments:
        P = pred[len(pred) // 2]  

        if min(seg[0] - L, seg[0]) < P < max(seg[-1] + L, seg[-1]):
            correct += 1  

    ratio = correct / (len(anomaly_segments) or 1)

    return correct, ratio 