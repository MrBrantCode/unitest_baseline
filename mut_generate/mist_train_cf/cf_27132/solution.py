"""
QUESTION:
Write a function `interpolateColor` that takes in the following parameters: 
- `rb`: a 2D array of color values at different time intervals, where `rb[i]` represents the color values at time `i`. Each color value is represented as a tuple `(red, green)`.
- `t0`: the time index for the lower bound of interpolation.
- `t`: the current time for which interpolation needs to be performed.
- `bright`: the brightness factor.

The function should return the interpolated color values `r` and `g` based on the given parameters. 

The interpolation formula for the red component `r` is `r = round((rb[t0][0] + (t-t0)*(rb[t0+1][0]-rb[t0][0]))*bright)>>8` and for the green component `g` is `g = round((rb[t0][1] + (t-t0)*(rb[t0+1][1]-rb[t0][1]))*bright)>>8`.
"""

def interpolateColor(rb, t0, t, bright):
    red_lower = rb[t0][0]
    green_lower = rb[t0][1]
    red_upper = rb[t0+1][0]
    green_upper = rb[t0+1][1]

    r = round((red_lower + (t-t0)*(red_upper-red_lower))*bright) >> 8
    g = round((green_lower + (t-t0)*(green_upper-green_lower))*bright) >> 8

    return r, g