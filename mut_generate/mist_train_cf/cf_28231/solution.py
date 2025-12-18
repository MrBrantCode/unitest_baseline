"""
QUESTION:
Implement the `calculate_total_anchors` function, which calculates the total number of anchors created based on the given parameters. The function takes the following parameters: 
- `scales`: An integer representing the number of scales for the anchors.
- `ratios`: A list of floats representing the aspect ratios for the anchors.
- `shape`: A list of two integers representing the shape of the feature map (height, width).
- `feature_stride`: An integer representing the stride of the feature map.
- `anchor_stride`: An integer representing the stride of the anchors.
The function should return the total number of anchors generated based on the provided parameters.
"""

def calculate_total_anchors(scales, ratios, shape, feature_stride, anchor_stride):
    """
    Calculate the total number of anchors created based on the given parameters.

    Parameters:
    scales (int): The number of scales for the anchors.
    ratios (list of floats): The aspect ratios for the anchors.
    shape (list of two integers): The shape of the feature map (height, width).
    feature_stride (int): The stride of the feature map.
    anchor_stride (int): The stride of the anchors.

    Returns:
    int: The total number of anchors generated based on the provided parameters.
    """
    total_anchors = 0
    for scale in range(scales):
        for ratio in ratios:
            height = shape[0]
            width = shape[1]
            for y in range(0, height * feature_stride, anchor_stride * feature_stride):
                for x in range(0, width * feature_stride, anchor_stride * feature_stride):
                    total_anchors += 1
    return total_anchors