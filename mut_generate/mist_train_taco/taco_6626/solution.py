"""
QUESTION:
Snuke has a calculator. It has a display and two buttons.

Initially, the display shows an integer x. Snuke wants to change this value into another integer y, by pressing the following two buttons some number of times in arbitrary order:

* Button A: When pressed, the value on the display is incremented by 1.
* Button B: When pressed, the sign of the value on the display is reversed.



Find the minimum number of times Snuke needs to press the buttons to achieve his objective. It can be shown that the objective is always achievable regardless of the values of the integers x and y.

Constraints

* x and y are integers.
* |x|, |y| ≤ 10^9
* x and y are different.

Input

The input is given from Standard Input in the following format:


x y


Output

Print the minimum number of times Snuke needs to press the buttons to achieve his objective.

Examples

Input

10 20


Output

10


Input

10 -10


Output

1


Input

-10 -20


Output

12
"""

def min_button_presses(x: int, y: int) -> int:
    ans = 10 ** 18
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    
    for i in range(4):
        tx = x * dx[i]
        ty = y * dy[i]
        if tx <= ty:
            ans = min(ans, ty - tx + (2 - dx[i] - dy[i]) // 2)
    
    return ans