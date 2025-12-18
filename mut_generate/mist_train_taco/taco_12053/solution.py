"""
QUESTION:
problem

AOR Ika made a set $ S = \\ {a_1, ..., a_N \\} $ and a map $ f: S → S $. $ f (a_i) = b_i $. For any element $ x $ in the set $ S $, all maps $ g, h: S → S $ satisfying $ g (f (x)) = h (f (x)) $ are $ g (x). ) = Determine if h (x) $ is satisfied, and if not, configure one counterexample.





Example

Input

5
1 2 3 4 5
3 4 2 5 1


Output

Yes
"""

def check_map_condition(N, A, F):
    from collections import Counter
    
    # Create a dictionary to map each element in A to its index
    Ad = {a: i for (i, a) in enumerate(A)}
    
    # Initialize a counter array to count occurrences of each element in F
    C = [0] * N
    
    # Count occurrences of each element in F
    for f in F:
        C[Ad[f]] += 1
    
    # Check if there is any element in C that is 0
    if 0 not in C:
        return True, None
    else:
        # Find the index of the first 0 in C (indicating a lack)
        lack = C.index(0)
        
        # Create a counterexample by modifying A
        ans = A[:lack] + [A[lack - 1]] + A[lack + 1:]
        
        return False, ans