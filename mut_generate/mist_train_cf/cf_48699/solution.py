"""
QUESTION:
Implement a function called `radial_blur_svg` that simulates a radial blur effect on a given SVG image without using the `<filter>` element. The function should accept an SVG image as input, and the output should be an SVG image with a radial blur effect applied. Note that the actual implementation may involve creating multiple copies of the image with decreasing opacity, and this approach might be complex for images with many colors and shapes.
"""

def radial_blur_svg(svg_image, num_copies, opacity_step):
    """
    Simulates a radial blur effect on a given SVG image by creating multiple copies 
    of the image with decreasing opacity.

    Args:
        svg_image (str): The input SVG image.
        num_copies (int): The number of copies to create.
        opacity_step (float): The step to decrease opacity by.

    Returns:
        str: The SVG image with a radial blur effect applied.
    """

    # Assuming svg_image is a string containing the SVG XML
    svg_xml = svg_image

    # Parse the SVG XML
    # For simplicity, this example uses basic string manipulation
    # In a real-world scenario, consider using an SVG parsing library
    svg_xml = svg_xml.strip()

    # Create multiple copies of the image with decreasing opacity
    blurred_svg = ""
    for i in range(num_copies):
        # Calculate the opacity for this copy
        opacity = 1.0 - (i * opacity_step)

        # Create a new copy of the image with the calculated opacity
        blurred_svg += f"<g opacity=\"{opacity}\">{svg_xml}</g>"

    return blurred_svg