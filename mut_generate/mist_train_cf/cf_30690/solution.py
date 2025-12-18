"""
QUESTION:
Implement a function `sort_files_by_stars` that takes a list of tuples as input, where each tuple contains a file path and a string representing the range of GitHub stars in the format "min-max". The function should return a sorted list of file paths based on the average of the star ranges. If two file paths have the same average star range, they should be sorted based on their file paths in ascending order.
"""

from typing import List, Tuple

def sort_files_by_stars(file_star_tuples: List[Tuple[str, str]]) -> List[str]:
    def get_average_stars(star_range: str) -> int:
        min_stars, max_stars = map(int, star_range.split('-'))
        return (min_stars + max_stars) // 2

    return sorted(file_star_tuples, key=lambda x: (get_average_stars(x[1]), x[0]))