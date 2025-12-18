"""
QUESTION:
Create a function `im2col` that takes a 3D tensor `image` with shape `(C, H, W)` representing an image with `C` channels, height `H`, and width `W`, and a filter with height `FH`, width `FW`, and stride `stride`. The function should return a 2D tensor `Dm` where each column represents a patch of size `FH` x `FW` from the input image, extracted by sliding the filter over the image with the given stride. The patches are flattened and stacked as columns in `Dm`. The height of `Dm` should be `C * FH * FW`.
"""

import numpy as np

def im2col(image, FH, FW, stride):
    C, H, W = image.shape
    OH = (H - FH) // stride + 1
    OW = (W - FW) // stride + 1
    Dm = np.zeros((C * FH * FW, OH * OW))
    for c in range(C):
        for h in range(FH):
            for w in range(FW):
                Dm[c * FH * FW + h * FW + w, :] = image[c, h:h+OH*stride:stride, w:w+OW*stride:stride].flatten()
    return Dm