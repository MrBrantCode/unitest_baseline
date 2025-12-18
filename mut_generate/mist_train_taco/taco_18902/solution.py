"""
QUESTION:
We have a pyramid with N steps, built with blocks. The steps are numbered 1 through N from top to bottom. For each 1≤i≤N, step i consists of 2i-1 blocks aligned horizontally. The pyramid is built so that the blocks at the centers of the steps are aligned vertically.

<image>

A pyramid with N=4 steps

Snuke wrote a permutation of (1, 2, ..., 2N-1) into the blocks of step N. Then, he wrote integers into all remaining blocks, under the following rule:

* The integer written into a block b must be equal to the median of the three integers written into the three blocks directly under b, or to the lower left or lower right of b.



<image>

Writing integers into the blocks

Afterwards, he erased all integers written into the blocks. Now, he only remembers that the integer written into the block of step 1 was x.

Construct a permutation of (1, 2, ..., 2N-1) that could have been written into the blocks of step N, or declare that Snuke's memory is incorrect and such a permutation does not exist.

Constraints

* 2≤N≤10^5
* 1≤x≤2N-1

Input

The input is given from Standard Input in the following format:


N x


Output

If no permutation of (1, 2, ..., 2N-1) could have been written into the blocks of step N, print `No`.

Otherwise, print `Yes` in the first line, then print 2N-1 lines in addition.

The i-th of these 2N-1 lines should contain the i-th element of a possible permutation.

Examples

Input

4 4


Output

Yes
1
6
3
7
4
5
2


Input

2 1


Output

No
"""

def construct_pyramid_permutation(N, x):
    """
    Constructs a permutation of (1, 2, ..., 2N-1) that could have been written into the blocks of step N,
    or declares that such a permutation does not exist based on the given constraints.

    Parameters:
    - N (int): The number of steps in the pyramid.
    - x (int): The integer written into the block of step 1.

    Returns:
    - tuple: A tuple containing a boolean (True if a valid permutation exists, False otherwise)
             and a list representing the permutation if it exists.
    """
    if x == 1 or x == 2 * N - 1:
        return False, []
    
    a = [None] * (2 * N - 1)
    m = (2 * N - 1) // 2
    a[m] = x
    a[m - 1] = x - 1
    a[m + 1] = x + 1
    vals = [x - 1, x, x + 1]
    
    if m + 2 < 2 * N - 1 and x - 2 >= 1:
        a[m + 2] = x - 2
        vals.append(x - 2)
    if m - 2 >= 0 and x + 2 <= 2 * N - 1:
        a[m - 2] = x + 2
        vals.append(x + 2)
    
    y = 1
    for i in range(2 * N - 1):
        if a[i] is not None:
            continue
        while y in vals:
            y += 1
        a[i] = y
        y += 1
    
    return True, a