"""
QUESTION:
Implement a function `detect_keypoints` that takes a 4-dimensional array `preds` of shape (N, H, W, C) as input, where N is the number of samples, H is the height of the feature map, W is the width of the feature map, and C is the number of channels (keypoint types). The function should iterate through the keypoints and return a list of detected keypoints, where each keypoint is represented as a tuple (x, y, confidence) containing the coordinates and confidence score of the detection.
"""

def detect_keypoints(preds):
    """
    Detects keypoints from a 4-dimensional array of predictions.

    Args:
    preds (numpy array): A 4-dimensional array of shape (N, H, W, C) containing keypoint predictions.

    Returns:
    list: A list of detected keypoints, where each keypoint is represented as a tuple (x, y, confidence).
    """
    points = []
    for i in range(preds.shape[3]):
        # Extract x, y coordinates, and confidence score for the ith keypoint
        x = preds[0, 0, 0, i]  
        y = preds[0, 0, 1, i]  
        confidence = preds[0, 0, 2, i]  
        points.append((x, y, confidence))
    return points