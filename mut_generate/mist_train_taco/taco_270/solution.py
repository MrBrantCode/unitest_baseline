"""
QUESTION:
Snuke loves puzzles.
Today, he is working on a puzzle using S- and c-shaped pieces.
In this puzzle, you can combine two c-shaped pieces into one S-shaped piece, as shown in the figure below:
Snuke decided to create as many Scc groups as possible by putting together one S-shaped piece and two c-shaped pieces.
Find the maximum number of Scc groups that can be created when Snuke has N S-shaped pieces and M c-shaped pieces.

-----Constraints-----
 - 1 ≤ N,M ≤ 10^{12}

-----Input-----
The input is given from Standard Input in the following format:
N M

-----Output-----
Print the answer.

-----Sample Input-----
1 6

-----Sample Output-----
2

Two Scc groups can be created as follows:
 - Combine two c-shaped pieces into one S-shaped piece
 - Create two Scc groups, each from one S-shaped piece and two c-shaped pieces
"""

def max_scc_groups(n: int, m: int) -> int:
    # Calculate the initial number of Scc groups that can be formed directly
    initial_groups = min(n, m // 2)
    
    # Calculate the remaining c-shaped pieces after forming the initial groups
    remaining_c_pieces = m - initial_groups * 2
    
    # Calculate additional Scc groups that can be formed with the remaining c-shaped pieces
    additional_groups = remaining_c_pieces // 4
    
    # Total number of Scc groups is the sum of initial and additional groups
    total_groups = initial_groups + additional_groups
    
    return total_groups