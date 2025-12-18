"""
QUESTION:
Implement the function `perform_image_cropping(img, top_left_pix, rc, raw_width, raw_height)` to extract a specified region from the input image `img` as a 2D array or matrix, where the cropped region is defined by the top-left corner coordinates `top_left_pix` and the relative bottom-right corner coordinates `rc` scaled by the raw dimensions `raw_width` and `raw_height` of the original image.
"""

def perform_image_cropping(img, top_left_pix, rc, raw_width, raw_height):
    bottom_right_pix = [int(rc[1][0] * raw_width), int(rc[1][1] * raw_height)]
    img_cropped = img[top_left_pix[1]:bottom_right_pix[1], top_left_pix[0]:bottom_right_pix[0]]
    return img_cropped