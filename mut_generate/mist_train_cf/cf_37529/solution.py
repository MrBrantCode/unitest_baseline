"""
QUESTION:
Implement a function `filter_largest_contours` that filters and returns the largest contours based on their relative areas. The function should take in four parameters: an array of floats `relative_areas` representing the relative areas of contours, an array of contours `top_contours`, and two floats `min_perc_area` and `max_perc_area` representing the minimum and maximum percentage area thresholds for the contours to be considered valid. The function should return two arrays: an array of contours representing the largest contours whose relative areas fall within the valid range, and an array of floats representing the relative areas of the largest contours.
"""

def filter_largest_contours(relative_areas, top_contours, min_perc_area, max_perc_area):
    # Convert input arrays to numpy arrays for efficient computation
    relative_areas = np.array(relative_areas)
    top_contours = np.array(top_contours)

    # Condition to check if area is within valid range
    cond_valid_area = (relative_areas >= min_perc_area) & (relative_areas <= max_perc_area)

    # Return the largest contours satisfying the valid area condition
    return top_contours[cond_valid_area], relative_areas[cond_valid_area]