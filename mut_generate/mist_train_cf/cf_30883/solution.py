"""
QUESTION:
Write a function `find_star_pairs` that takes in three parameters: `camera_position` (float), `unique_check` (bool), and `star_catalogue` (List[Tuple[str, float, float]]). The function should return a list of tuples, where each tuple contains the names of two stars that could potentially be observed together in an image.

The function should consider the following conditions:
- The distance between the camera and each star should be less than or equal to 10,000 kilometers.
- If `unique_check` is True, a star should not be paired with itself.

The camera position is in kilometers with respect to the solar system barycenter in the inertial frame. Each star in the catalogue is represented as a tuple containing the star's name (a string) and its position in the inertial frame as (x, y) coordinates in kilometers.
"""

from typing import List, Tuple

def find_star_pairs(camera_position: float, unique_check: bool, star_catalogue: List[Tuple[str, float, float]]) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(len(star_catalogue)):
        for j in range(i+1, len(star_catalogue)):
            star1_name, star1_x, star1_y = star_catalogue[i]
            star2_name, star2_x, star2_y = star_catalogue[j]
            dist1 = ((camera_position - star1_x) ** 2 + (0 - star1_y) ** 2) ** 0.5
            dist2 = ((camera_position - star2_x) ** 2 + (0 - star2_y) ** 2) ** 0.5
            if dist1 <= 10000 and dist2 <= 10000:
                if unique_check and star1_name == star2_name:
                    continue
                pairs.append((star1_name, star2_name))
    return pairs