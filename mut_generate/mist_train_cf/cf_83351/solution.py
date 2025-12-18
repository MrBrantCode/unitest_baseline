"""
QUESTION:
Create a function named "regular_pyramid_surface_area" that takes three parameters: the side length "s" of the base, the number of sides "n" of the base, and the height "h" of the pyramid. The function should calculate the surface area of the regular n-sided 3D pyramid using the Pythagorean theorem for the slant height and return the result. The base is a regular polygon with "n" sides, each of length "s", and the pyramid's height is "h".
"""

import math

def regular_pyramid_surface_area(s, n, h):
  # calculates the slant height (l)
  l = math.sqrt((s / (2 * math.tan(math.pi/n))) ** 2 + h ** 2)
  # calculates the base perimeter (P)
  P = n * s
  # calculates the base area (A)
  A = (P * s) / (4 * math.tan(math.pi/n))
  
  # calculates the pyramid surface area
  surface_area = (P * l) / 2 + A

  return surface_area