"""
QUESTION:
Write a function called `aug_min_length` that takes in two parameters: `det_lines_pos` and `obj_rep`. The function should return the minimum length between the two parameters. Do not use any external libraries and do not assume any specific data type for the input parameters.
"""

def aug_min_length(det_lines_pos, obj_rep):
    if isinstance(det_lines_pos, list):
        det_lines_pos = det_lines_pos[0]
    if isinstance(obj_rep, list):
        obj_rep = obj_rep[0]
    det_lines_pos = abs(det_lines_pos)
    obj_rep = abs(obj_rep)
    return min(det_lines_pos, obj_rep)