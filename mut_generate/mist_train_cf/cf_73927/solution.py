"""
QUESTION:
Given the ratio of (2x - y) to (x + y) is 2 to 3, find the simplified fraction ratio of x to y when x is greater than y.
"""

def entrance(x, y):
    return "%.0f:%.0f" % (x,y) if x > y else "%d:%d" % (y,x)

# Algebraic solution
def algebraic_entrance(x, y):
    return "5:4"