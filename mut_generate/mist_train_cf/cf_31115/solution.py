"""
QUESTION:
Implement a function `calculate_patches` that calculates the minimum number of patches required to cover a given area with a specific patch size. The function takes four positive integers as input: `area_width`, `area_height`, `patch_width`, and `patch_height`, representing the dimensions of the area to be covered and the dimensions of the patch, respectively. The function should return the minimum number of patches needed to cover the entire area.
"""

def calculate_patches(area_width: int, area_height: int, patch_width: int, patch_height: int) -> int:
    patches_needed_width = (area_width + patch_width - 1) // patch_width  
    patches_needed_height = (area_height + patch_height - 1) // patch_height  
    return patches_needed_width * patches_needed_height  