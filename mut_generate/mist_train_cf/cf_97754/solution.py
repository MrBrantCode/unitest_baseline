"""
QUESTION:
Create a Python function named `get_bounding_box_pixels` that receives as input an image and the bounding box of a detected object in that image, and returns a list of the RGB values of all pixels within the bounding box. The input image is represented as a numpy array and the bounding box is a tuple in the format (x, y, w, h), where (x, y) are the coordinates of the top left corner of the bounding box, and (w, h) are the width and height of the bounding box. The function should return a list of tuples, where each tuple represents the RGB values of a pixel within the bounding box, in the format (R, G, B).
"""

def get_bounding_box_pixels(img, bbox):
    """
    Receives an image and the bounding box of a detected object in that image, and returns a list of the RGB values of all pixels within the bounding box.
    
    Parameters:
    img (numpy array): The input image, represented as a numpy array.
    bbox (tuple): A tuple representing the bounding box of the object in the format (x, y, w, h),
    where (x, y) are the coordinates of the top left corner of the bounding box, and (w, h) are the width and height of the bounding box.
    
    Returns:
    list: A list of tuples, where each tuple represents the RGB values of a pixel within the bounding box, in the format (R, G, B).
    """
    x, y, w, h = bbox
    roi = img[y:y+h, x:x+w]
    return [tuple(pixel) for row in roi for pixel in row]