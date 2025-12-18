"""
QUESTION:
Create a function named `carpet_coverage` that calculates the carpet area required to cover a rectangular room. The function should accept three parameters: `length` (the length of the room), `width` (the width of the room), and `coverage` (the ratio of the room's area that the carpet should cover). The function should return the carpet area if the inputs are valid and error messages otherwise. The function should handle cases where `length`, `width`, or `coverage` are zero, negative, or if `coverage` exceeds 1 (100%).
"""

def carpet_coverage(length, width, coverage):
    # Validate the input values
    if length < 0 or width < 0 or coverage < 0:
        return 'Invalid input! Dimensions and coverage should be non-negative.'
    if coverage > 1:
        return 'Invalid input! Carpet coverage should not exceed 100%.'
    
    room_area = length * width
    carpet_area = room_area * coverage
    return carpet_area