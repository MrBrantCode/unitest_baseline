"""
QUESTION:
Draw a frame which has a height of H cm and a width of W cm. For example, the following figure shows a frame which has a height of 6 cm and a width of 10 cm.



........#
........#
........#
........#



Constraints

* 3 ≤ H ≤ 300
* 3 ≤ W ≤ 300

Input

The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output

For each dataset, print the frame made of '#' and '.'.

Print a blank line after each dataset.

Example

Input

3 4
5 6
3 3
0 0


Output

####
#..#
####

######
#....#
#....#
#....#
######

###
#.#
###
"""

def draw_frame(H, W):
    if H == 0 and W == 0:
        return []
    
    top_bottom_row = '#' * W
    middle_row = '#' + '.' * (W - 2) + '#'
    
    frame = [top_bottom_row] + [middle_row] * (H - 2) + [top_bottom_row]
    
    return frame + ['']