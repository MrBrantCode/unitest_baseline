"""
QUESTION:
Implement the function `validate_ray_behavior(ray, surface, expected_n, expected_direction)` that takes in a `ray` object, a `surface` it interacts with, the expected refractive index `expected_n` after interaction, and the expected direction vector `expected_direction` of the ray after interaction. The function should return `True` if the ray's behavior matches the expected values and `False` otherwise. Ensure that the number of segments after tracing the ray through the surface is 2, the refractive index of the ray after interaction matches `expected_n`, and the direction vector of the ray after interaction matches `expected_direction`.
"""

def validate_ray_behavior(ray, surface, expected_n, expected_direction):
    segments = ray.trace_surfaces((surface,), ('transmitted', ))[0]
    if len(segments) == 2 and segments[-1].ray.n == expected_n and np.allclose(segments[-1].ray.line.vector, expected_direction):
        return True
    else:
        return False