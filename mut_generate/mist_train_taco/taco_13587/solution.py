"""
QUESTION:
For given a sequence $A = \\{a_0, a_1, ..., a_{n-1}\\}$, print the previous permutation and the next permutation in lexicographic order.

Constraints

* $1 \leq n \leq 9$
* $a_i$ consist of $1, 2, ..., n$

Input

A sequence is given in the following format.


$n$
$a_0 \; a_1 \; ... \; a_{n-1}$


Output

Print the previous permutation, the given sequence and the next permutation in the 1st, 2nd and 3rd lines respectively. Separate adjacency elements by a space character. Note that if there is no permutation, print nothing in the corresponding line.

Examples

Input

3
2 1 3


Output

1 3 2
2 1 3
2 3 1


Input

3
3 2 1


Output

3 1 2
3 2 1
"""

import operator

def generate_permutations(sequence):
    def perm(op):
        def func(xs):
            i = len(xs) - 1
            while i > 0 and op(xs[i - 1], xs[i]):
                i -= 1
            if i > 0:
                i -= 1
                j = i + 1
                while j < len(xs) and op(xs[j], xs[i]):
                    j += 1
                (xs[i], xs[j - 1]) = (xs[j - 1], xs[i])
                return xs[:i + 1] + list(reversed(xs[i + 1:]))
            else:
                return None
        return func
    
    prev_perm = perm(operator.lt)
    next_perm = perm(operator.gt)
    
    result = []
    
    pp = prev_perm(sequence[:])
    if pp is not None:
        result.append(pp)
    else:
        result.append(None)
    
    result.append(sequence[:])
    
    np = next_perm(sequence[:])
    if np is not None:
        result.append(np)
    else:
        result.append(None)
    
    return result