"""
QUESTION:
Create a function named `transform_svg` that takes an SVG string as input and returns an SVG string with the added animations or effects that make the SVG appear as a magical portal, specifically shimmer and swirl.
"""

def transform_svg(svg_string):
    """
    Adds shimmer and swirl effects to an SVG string using CSS animations.

    Args:
        svg_string (str): The input SVG string.

    Returns:
        str: The modified SVG string with added animations.
    """
    # Add CSS styles for shimmer and swirl effects
    style = """
    <style>
    .shimmer {
        animation: shimmer 2s infinite;
    }
    @keyframes shimmer {
        0% {
            transform: translateX(0);
        }
        100% {
            transform: translateX(100%);
        }
    }
    .swirl {
        animation: swirl 4s infinite;
    }
    @keyframes swirl {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
    </style>
    """

    # Add classes to SVG elements for animation
    svg_string = svg_string.replace("<svg", "<svg class='shimmer swirl'")

    # Combine the style and the modified SVG string
    transformed_svg = style + svg_string

    return transformed_svg