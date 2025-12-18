"""
QUESTION:
Gag

Segtree has $ N $ of "gags", each with a value of $ V_i $.

Segtree decided to publish all the gags in any order.

Here, the "joy" you get when you publish the $ i $ th gag to the $ j $ th is expressed as $ V_i --j $.

Find the maximum sum of the "joy" you can get.

input

Input is given from standard input in the following format.


$ N $
$ V_1 $ $ V_2 $ $ \ ldots $ $ V_N $


output

Please output the maximum value of the sum of "joy". However, the value does not always fit in a 32-bit integer.

Insert a line break at the end.

Constraint

* $ 1 \ leq N \ leq 10 ^ 5 $
* $ 1 \ leq V_i \ leq 10 ^ 5 $
* All inputs are integers.



Input example 1


1
59549


Output example 1


59548


Input example 2


Five
2 1 8 5 7


Output example 2


8






Example

Input

1
59549


Output

59548
"""

def calculate_max_joy(N, V):
    count = 0
    ans = 0
    s = -1
    while count != N:
        ans -= s
        s -= 1
        count += 1
    return sum(V) - ans