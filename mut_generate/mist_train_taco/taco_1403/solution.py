"""
QUESTION:
Times Square in the capital city of NY  has a rectangular shape with the size n × m meters. On the occasion of the city's anniversary, a decision was taken to pave the Square with square granite flagstones. Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square? It's allowed to cover the surface larger than the Times Square, but the Square has to be covered. It's not allowed to break the flagstones. The sides of flagstones should be parallel to the sides of the Square.
Input

The input contains three positive integer numbers in the first line: n,  m and a (1 ≤  n, m, a ≤ 109).
Output

Write the needed number of flagstones.

SAMPLE INPUT
6 6 4

SAMPLE OUTPUT
4
"""

def calculate_flagstones(n: int, m: int, a: int) -> int:
    def ceiling(x, y):
        div = x // y
        res = x % y
        if res != 0:
            div += 1
        return div
    
    num1 = ceiling(n, a)
    num2 = ceiling(m, a)
    return num1 * num2