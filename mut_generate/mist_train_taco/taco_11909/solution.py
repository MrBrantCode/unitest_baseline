"""
QUESTION:
Bob needs a fast way to calculate the volume of a cuboid with three values: `length`, `width` and the `height` of the cuboid. Write a function to help Bob with this calculation.

```if:shell
In bash the script is ran with the following 3 arguments:
`length` `width` `height`
```
"""

def calculate_cuboid_volume(length, width, height):
    """
    Calculate the volume of a cuboid given its length, width, and height.

    Parameters:
    length (float or int): The length of the cuboid.
    width (float or int): The width of the cuboid.
    height (float or int): The height of the cuboid.

    Returns:
    float or int: The volume of the cuboid.
    """
    return length * width * height