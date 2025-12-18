"""
QUESTION:
Implement the `calculate_overlap_area` function that takes the geographic boundaries of two raster images as input and returns the area of overlap between them. The function should accept the minimum latitude, maximum latitude, minimum longitude, and maximum longitude of each raster image as parameters. Calculate the area in square degrees. Assume the input geographic boundaries are valid and the Earth is flat within the scope of the problem. The function should return 0 if there is no overlap between the two images.
"""

def calculate_overlap_area(min_lat1, max_lat1, min_long1, max_long1, min_lat2, max_lat2, min_long2, max_long2):
    # Calculate the overlapping latitude range
    overlap_lat_min = max(min_lat1, min_lat2)
    overlap_lat_max = min(max_lat1, max_lat2)

    # Calculate the overlapping longitude range
    overlap_long_min = max(min_long1, min_long2)
    overlap_long_max = min(max_long1, max_long2)

    # Check if there is actual overlap between the rectangles
    if overlap_lat_max < overlap_lat_min or overlap_long_max < overlap_long_min:
        return 0  # No overlap, so the area is 0

    # Calculate the width and height of the overlapping area
    overlap_width = overlap_long_max - overlap_long_min
    overlap_height = overlap_lat_max - overlap_lat_min

    # Calculate the area of overlap using the formula: area = width * height
    overlap_area = overlap_width * overlap_height

    return overlap_area