"""
QUESTION:
Write a function `cuboid_surface_area` that calculates the surface area of a three-dimensional rectangular cuboid before and after applying a layer of coating. The function should take four parameters: the original length, breadth, and stature of the cuboid, and an optional parameter for the thickness of the coating (defaulting to 0). The coating is assumed to be applied evenly on all six faces of the cuboid and does not consume space from the actual cuboid. The function should return the surface area of the cuboid considering the layer of coating.
"""

def cuboid_surface_area(length, breadth, stature, coating=0):
    # Calculates the surface area 
    # considering the layer of coating
    length += 2*coating
    breadth += 2*coating
    stature += 2*coating
    surface_area = 2*(length * breadth +
                    breadth * stature +
                    stature * length)
    return surface_area