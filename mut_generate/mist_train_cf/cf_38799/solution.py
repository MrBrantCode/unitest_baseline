"""
QUESTION:
Implement a decorator function `colorize_output(hue_shift, saturation_scale, lightness_scale)` that takes a function as input and applies a color transformation to its output. The function should transform the numerical output into an HSL color representation using the `colorsys` module, then convert the HSL to RGB and print the RGB values to the console. The transformation should be applied according to the provided `hue_shift`, `saturation_scale`, and `lightness_scale` parameters. The decorator should also preserve the original function's metadata.
"""

import colorsys as _coloursys
from functools import wraps

def entance(hue_shift, saturation_scale, lightness_scale):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            hue = (result * hue_shift) % 1.0
            saturation = min(1.0, max(0.0, result * saturation_scale))
            lightness = min(1.0, max(0.0, result * lightness_scale))
            r, g, b = _coloursys.hls_to_rgb(hue, lightness, saturation)
            print(f"RGB: ({round(r * 255)}, {round(g * 255)}, {round(b * 255)})")
        return wrapper
    return decorator