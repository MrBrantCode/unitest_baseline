"""
QUESTION:
Write a Python function `generate_macros(gl, wgl, glX)` that takes three input lists `gl`, `wgl`, and `glX` and returns a string containing macro definitions. The input lists consist of sublists, where each sublist represents a function and its return type. The return type is stored as the first element of the sublist. 

The macro definitions should include the end index of `gl`, the start and end indices of `wgl`, the start and end indices of `glX`, and the return types of the functions in the input lists, in the format `define('name', 'value')`. 

The indices are 0-based and the end index of a list is one less than the start index of the next list.
"""

def entrance(gl, wgl, glX):
    macro_definitions = []

    # Write out the end indices for gl, wgl, and glX
    macro_definitions.append('define(`gl_end`, `%d`)' % (len(gl) - 1))
    macro_definitions.append('define(`wgl_start`, `%d`)' % len(gl))
    macro_definitions.append('define(`wgl_end`, `%d`)' % (len(gl) + len(wgl) - 1))
    macro_definitions.append('define(`glX_start`, `%d`)' % (len(gl) + len(wgl)))
    macro_definitions.append('define(`glX_end`, `%d`)' % (len(gl) + len(wgl) + len(glX) - 1))

    # Write out the return types for each function
    i = 0
    for l in (gl, wgl, glX):
        for t in l:
            # Process return type to strip trailing spaces
            t[0] = t[0].strip()
            macro_definitions.append('define(`f%d_ret`, `%s`)' % (i, t[0]))
            i += 1

    return '\n'.join(macro_definitions)