"""
QUESTION:
Given a string `color` of length 7 representing an RGB color, find a 7 character color string that exhibits the highest similarity to `color` and can be expressed in shorthand form. The similarity between two colors `#ABCDEF` and `#UVWXYZ` is defined as `-(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2`. The output should be a string of length 7 in lowercase letters.
"""

def similarRGB(color):
    def closest(s):
        q, r = divmod(int(s, 16), 17)
        if r > 8: q += 1
        return '{:02x}'.format(17 * q)

    return '#' + ''.join(closest(color[i:i+2]) for i in (1, 3, 5))