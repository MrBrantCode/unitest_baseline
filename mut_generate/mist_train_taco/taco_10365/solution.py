"""
QUESTION:
problem

There is a mysterious device $ M $, and if you put Tanuki and Fox in this device, one animal will come out from the device (hereinafter, Tanuki will be $ T $ and Fox will be $ F $).

$ M (x, y) $ represents an animal that came out by putting animals in the device $ M $ in the order of $ x, y $.

As a result of various trials, the following was found.


$ M (T, T) = T $
$ M (T, F) = F $
$ M (F, T) = T $
$ M (F, F) = T $



You put the animals in a row $ P_1, P_2, ..., P_N $ into the device as follows.
$ M (.... M (M (P_1, P_2), P_3) ...., P_N) $

Answer the last animal that appears.



output

Output the last animal character $ T $ or $ F $, and also a newline at the end.

Example

Input

3
F T T


Output

T
"""

from functools import reduce

def M(x, y):
    if x == 'T' and y == 'T':
        return 'T'
    elif x == 'T' and y == 'F':
        return 'F'
    elif x == 'F' and y == 'T':
        return 'T'
    else:
        return 'T'

def process_animals(N, P):
    return reduce(M, P)