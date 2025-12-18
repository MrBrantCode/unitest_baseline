"""
QUESTION:
Implement a function `paste_with_alpha` that overlays a smaller image onto a larger image using alpha blending. The function should take in three parameters: `larger` (the larger image), `smaller` (the smaller image), and `xy` (the coordinates at which to place the smaller image). The function should return the modified larger image with the smaller image smoothly overlaid onto it. The images are represented as 3D arrays with shape `(height, width, 4)`, where the fourth channel represents the alpha (transparency) value.
"""

def paste_with_alpha(larger, smaller, xy):
    x, y = xy
    x_end, y_end = x + smaller.shape[1], y + smaller.shape[0]

    alpha_s = smaller[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        larger[y:y_end, x:x_end, c] = (alpha_s * smaller[:, :, c] +
                                       alpha_l * larger[y:y_end, x:x_end, c])

    return larger