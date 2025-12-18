"""
QUESTION:
This is the simple version of [Fastest Code : Equal to 24](http://www.codewars.com/kata/574e890e296e412a0400149c). 

## Task

A game I played when I was young: Draw 4 cards from playing cards, use ```+ - * / and ()``` to make the final results equal to 24.

You will coding in function ```equalTo24```. Function accept 4 parameters ```a b c d```(4 cards), value range is 1-13.

The result is a string such as ```"2*2*2*3"``` ,```(4+2)*(5-1)```; If it is not possible to calculate the 24, please return "It's not possible!"

All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.

## Examples
"""

from itertools import permutations

def equal_to_24(a, b, c, d):
    ops = '+-*/'
    for b_op in ops:
        for d_op in ops:
            for f_op in ops:
                for (a_val, c_val, e_val, g_val) in permutations((a, b, c, d)):
                    for s in make_string(a_val, b_op, c_val, d_op, e_val, f_op, g_val):
                        try:
                            if eval(s + '== 24'):
                                return s
                        except:
                            pass
    return "It's not possible!"

def make_string(a, b, c, d, e, f, g):
    return [
        f'(({a} {b} {c}) {d} {e}) {f} {g}',
        f'({a} {b} {c}) {d} ({e} {f} {g})',
        f'{a} {b} ({c} {d} ({e} {f} {g}))'
    ]