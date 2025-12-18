"""
QUESTION:
Hey, Path Finder, where are you?

## Path Finder Series:
-       [#1: can you reach the exit?](https://www.codewars.com/kata/5765870e190b1472ec0022a2)
-       [#2: shortest path](https://www.codewars.com/kata/57658bfa28ed87ecfa00058a)
-       [#3: the Alpinist](https://www.codewars.com/kata/576986639772456f6f00030c)
-       [#4: where are you?](https://www.codewars.com/kata/5a0573c446d8435b8e00009f)
-       [#5: there's someone here](https://www.codewars.com/kata/5a05969cba2a14e541000129)
"""

import re

def find_my_location(path):
    class Me(object):
        def __init__(self):
            (self.x, self.y, self.dx, self.dy) = (0, 0, -1, 0)

        def move(self, n):
            self.x += n * self.dx
            self.y += n * self.dy

        def back(self):
            self.dx *= -1
            self.dy *= -1

        def turn(self, d):
            (self.dx, self.dy) = (self.dy * (-1) ** (d == 'l'), 0) if self.dy else (0, self.dx * (-1) ** (d == 'r'))

        def where(self):
            return [self.x, self.y]

    me = Me()
    
    for v in re.findall('\\d+|.', path):
        if v in 'RL':
            me.back()
        elif v in 'rl':
            me.turn(v)
        else:
            me.move(int(v))
    
    return me.where()