"""
QUESTION:
Snuke loves puzzles.

Today, he is working on a puzzle using `S`- and `c`-shaped pieces. In this puzzle, you can combine two `c`-shaped pieces into one `S`-shaped piece, as shown in the figure below:

9b0bd546db9f28b4093d417b8f274124.png

Snuke decided to create as many `Scc` groups as possible by putting together one `S`-shaped piece and two `c`-shaped pieces.

Find the maximum number of `Scc` groups that can be created when Snuke has N `S`-shaped pieces and M `c`-shaped pieces.

Constraints

* 1 ≤ N,M ≤ 10^{12}

Input

The input is given from Standard Input in the following format:


N M


Output

Print the answer.

Examples

Input

1 6


Output

2


Input

12345 678901


Output

175897
"""

def max_scc_groups(N, M):
    # Calculate the initial number of Scc groups that can be formed
    p = min(N, M // 2)
    
    # Update the number of c-shaped pieces left after forming p groups
    M -= p * 2
    
    # Calculate additional Scc groups that can be formed with remaining c-shaped pieces
    ans = p + M // 4
    
    return ans