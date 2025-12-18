"""
QUESTION:
Implement the function `apply_transformations(image, operations)` where `image` is a 2D list representing the original image and `operations` is a list of dictionaries representing the transformation operations. Each operation dictionary contains a `type` key indicating the type of transformation and additional keys for specific transformation parameters. The supported transformation types include 'Resize', 'Rotate', and 'Crop'. The function should return the transformed image after applying all the specified operations. 

The 'Resize' transformation dictionary contains a 'size' key whose value is a tuple representing the new dimensions of the image. If one of the dimensions is set to -1, it means that the aspect ratio should be preserved based on the other dimension. The 'Rotate' transformation dictionary contains an 'angle' key representing the angle of rotation in degrees. The 'Crop' transformation dictionary contains 'left', 'top', 'width', and 'height' keys representing the coordinates and dimensions of the cropping rectangle.
"""

def apply_transformations(image, operations):
    transformed_image = image
    for operation in operations:
        if operation['type'] == 'Resize':
            size = operation['size']
            if size[0] == -1:
                ratio = size[1] / len(transformed_image)
                new_width = int(len(transformed_image[0]) * ratio)
                transformed_image = [row[:new_width] for row in transformed_image]
            elif size[1] == -1:
                ratio = size[0] / len(transformed_image[0])
                new_height = int(len(transformed_image) * ratio)
                transformed_image = transformed_image[:new_height]
            else:
                transformed_image = [row[:size[0]] for row in transformed_image[:size[1]]]

        elif operation['type'] == 'Rotate':
            angle = operation['angle']
            if angle == 90:
                transformed_image = [list(row) for row in zip(*reversed(transformed_image))]
            elif angle == 180:
                transformed_image = [list(reversed(row)) for row in reversed(transformed_image)]
            elif angle == 270:
                transformed_image = [list(row) for row in zip(*transformed_image)]
                transformed_image.reverse()

        elif operation['type'] == 'Crop':
            left, top, width, height = operation['left'], operation['top'], operation['width'], operation['height']
            transformed_image = [row[left:left+width] for row in transformed_image[top:top+height]]

    return transformed_image