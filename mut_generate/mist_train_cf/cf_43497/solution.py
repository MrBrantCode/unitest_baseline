"""
QUESTION:
Separate Color and Brightness in Reflections for a Custom Shader Function

Create a function that allows reflections to influence only the colors of an object's screen pixels, without affecting their brightness. The function should treat reflections similar to a Material's Albedo (texture), where the Metallic value does not uniformly fully light surfaces when set to 1.
"""

def separate_color_brightness(reflection, color, brightness):
    # In a physically accurate rendering model, this would not be possible
    # as reflection influences both color and brightness.
    # However, we can simulate this by not changing the brightness.
    return color * reflection, brightness