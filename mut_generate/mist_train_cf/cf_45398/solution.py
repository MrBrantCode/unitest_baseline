"""
QUESTION:
Write a function named `volume_of_truncated_pyramid` that takes three parameters: the side length of the square base, the total height of the pyramid, and the height at which the pyramid is truncated. The function should calculate the volume of the truncated pyramid, which is the difference between the volume of the original pyramid and the volume of the smaller pyramid. The volume of a pyramid is given by the formula `1/3 * base_area * height`, where the base area is the square of the base side length. The height at which the pyramid is truncated should be between 0 and the total height of the pyramid.
"""

def volume_of_truncated_pyramid(base_side_length, total_height, truncated_height):
    return (1/3 * (base_side_length ** 2) * total_height) - (1/3 * ((base_side_length / total_height) * truncated_height) ** 2 * truncated_height)