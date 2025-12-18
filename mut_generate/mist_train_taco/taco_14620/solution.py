"""
QUESTION:
Snuke stands on a number line. He has L ears, and he will walk along the line continuously under the following conditions:

* He never visits a point with coordinate less than 0, or a point with coordinate greater than L.
* He starts walking at a point with integer coordinate, and also finishes walking at a point with integer coordinate.
* He only changes direction at a point with integer coordinate.



Each time when Snuke passes a point with coordinate i-0.5, where i is an integer, he put a stone in his i-th ear.

After Snuke finishes walking, Ringo will repeat the following operations in some order so that, for each i, Snuke's i-th ear contains A_i stones:

* Put a stone in one of Snuke's ears.
* Remove a stone from one of Snuke's ears.



Find the minimum number of operations required when Ringo can freely decide how Snuke walks.

Constraints

* 1 \leq L \leq 2\times 10^5
* 0 \leq A_i \leq 10^9(1\leq i\leq L)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


L
A_1
:
A_L


Output

Print the minimum number of operations required when Ringo can freely decide how Snuke walks.

Examples

Input

4
1
0
2
3


Output

1


Input

8
2
0
0
2
1
3
4
1


Output

3


Input

7
314159265
358979323
846264338
327950288
419716939
937510582
0


Output

1
"""

def minimum_operations_to_balance_ears(L, A):
    # Helper function to determine the cost based on the number of stones
    def zot(x):
        return 0 if x == 0 else (x + 1) % 2 + 1
    
    # Initialize the D array with zeros
    D = [0, 0, 0, 0, 0]
    
    # Iterate over each element in A
    for a in A:
        d0 = D[0] + a
        d1 = min(D[:2]) + [2, 1, 0][zot(a)]
        d2 = min(D[:3]) + [1, 0, 1][zot(a)]
        d3 = min(D[:4]) + [2, 1, 0][zot(a)]
        d4 = min(D) + a
        D = [d0, d1, d2, d3, d4]
    
    # Return the minimum value in D, which represents the minimum number of operations
    return min(D)