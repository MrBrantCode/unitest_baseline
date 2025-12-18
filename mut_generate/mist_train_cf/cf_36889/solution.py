"""
QUESTION:
Implement the function `shiftCoordinates(grid, lonShift, latShift)` that takes a 2D array `grid` of geographical coordinates as [latitude, longitude] pairs, and two integer values `lonShift` and `latShift`. The function should shift the longitude values by `lonShift` without changing the latitude values, wrapping around to the opposite side if the shifted longitude values exceed the bounds of the valid range (-180 to 180). Return the modified grid.
"""

def shift_coordinates(grid, lon_shift, lat_shift):
    for i in range(len(grid)):
        grid[i][1] += lon_shift
        if grid[i][1] > 180:
            grid[i][1] = -180 + (grid[i][1] - 180)
        elif grid[i][1] < -180:
            grid[i][1] = 180 + (grid[i][1] + 180)
    return grid