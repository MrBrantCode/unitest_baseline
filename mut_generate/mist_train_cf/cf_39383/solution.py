"""
QUESTION:
Implement the FontMetrics class with the following requirements:

- The class has an initializer that accepts values for 'x-height', 'cap-height', 'ascent', 'descent', 'pixel-size', 'direction', 'offset', and 'tracking'.
- The class has a method named 'update_offset' that takes two integer arguments and updates the 'offset' attribute with the new values.
- The class has a method named 'change_direction' that takes a string argument and updates the 'direction' attribute with the new value.
- The class has a method named 'get_pixel_size' that returns the sum of 'ascent' and 'descent'.
- Ensure that the class attributes are properly encapsulated and accessible only through appropriate methods.
"""

def font_metrics(x_height, cap_height, ascent, descent, pixel_size, direction, offset, tracking):
    font = {
        'x-height': x_height,
        'cap-height': cap_height,
        'ascent': ascent,
        'descent': descent,
        'pixel-size': pixel_size,
        'direction': direction,
        'offset': offset,
        'tracking': tracking
    }
    def update_offset(horiz_offset, vert_offset):
        nonlocal font
        font['offset'] = (horiz_offset, vert_offset)
    def change_direction(new_direction):
        nonlocal font
        font['direction'] = new_direction
    def get_pixel_size():
        nonlocal font
        return font['ascent'] + font['descent']
    return update_offset, change_direction, get_pixel_size