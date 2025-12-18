"""
QUESTION:
Design a function `rotate_hypercube` that takes an n-dimensional hypercube as input, represented as a series of n-1 dimensional matrices, and returns the hypercube rotated 90 degrees around its central axis, layer by layer, starting from the outermost layer inward. The rotation should maintain the shape of the hypercube invariant but change the position of the points to reflect a 90-degree rotation.
"""

def rotate_hypercube(hypercube):
    rotate_layer = lambda layer: [list(x) for x in zip(*layer[::-1])]
    return [rotate_layer(layer) for layer in hypercube]