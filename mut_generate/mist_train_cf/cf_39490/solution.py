"""
QUESTION:
Write a Python function `convert_to_array(colors, c_name)` that takes a list of RGB tuples `colors` and a string `c_name` as input. Each RGB tuple contains three integers in the range [0, 255] representing the red, green, and blue components of the color. The function should convert each RGB tuple to an integer using the formula `c[0] * 2**16 + c[1] * 2**8 + c[2]`, join the converted integers with a comma and space, and prefix each integer with "0x" to represent it in hexadecimal format. The resulting string should be split into lines of 80 characters each and printed in the format `static final int[] c_name = { ... };`.
"""

def convert_to_array(colors, c_name):
    s = ", ".join([("0x%06x" % (c[0] * 2**16 + c[1] * 2**8 + c[2])) for c in colors])
    s2 = '\n'.join([s[0+i:80+i] for i in range(0, len(s), 80)])
    return "static final int[] " + c_name + " = {\n" + s2 + "\n};\n"