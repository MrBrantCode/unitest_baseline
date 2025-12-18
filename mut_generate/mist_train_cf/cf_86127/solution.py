"""
QUESTION:
Implement a function `triplet_loss(margin, positive_distance, negative_distance)` that calculates the triplet loss given a margin constant, the distance between similar features (positive_distance), and the distance between dissimilar features (negative_distance). The function should return the calculated loss value. Assume the margin constant is used to increase the distance between similar and dissimilar features, and the loss is zero if the difference between the distances is greater than the margin.
"""

def triplet_loss(margin, positive_distance, negative_distance):
    return max(0, margin + positive_distance - negative_distance)