"""
QUESTION:
Create a function called `age_svg` that takes an SVG string as input and returns the SVG string with a weathered look. The function should use SVG filters, patterns, or other techniques to give the SVG a weathered appearance. The function should not require any external libraries or software, and should only use standard SVG syntax.
"""

def age_svg(svg_string):
    # Parse the SVG string to add filters, patterns, and other effects
    # For this example, let's add a simple filter to give a weathered look
    filter_string = """
    <filter id="weathered" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.1" numOctaves="5" seed="1234" />
      <feDisplacementMap in="SourceGraphic" in2="turbulence" scale="20" xChannelSelector="R" yChannelSelector="G" />
    </filter>
    """

    # Add the filter to the SVG string
    svg_string = svg_string.replace("<svg", "<svg><defs>" + filter_string + "</defs>")

    # Apply the filter to the SVG elements
    svg_string = svg_string.replace("<path", '<path filter="url(#weathered)"')

    return svg_string