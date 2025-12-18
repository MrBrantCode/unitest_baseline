"""
QUESTION:
Toad Ivan has $m$ pairs of integers, each integer is between $1$ and $n$, inclusive. The pairs are $(a_1, b_1), (a_2, b_2), \ldots, (a_m, b_m)$. 

He asks you to check if there exist two integers $x$ and $y$ ($1 \leq x < y \leq n$) such that in each given pair at least one integer is equal to $x$ or $y$.


-----Input-----

The first line contains two space-separated integers $n$ and $m$ ($2 \leq n \leq 300\,000$, $1 \leq m \leq 300\,000$) — the upper bound on the values of integers in the pairs, and the number of given pairs.

The next $m$ lines contain two integers each, the $i$-th of them contains two space-separated integers $a_i$ and $b_i$ ($1 \leq a_i, b_i \leq n, a_i \neq b_i$) — the integers in the $i$-th pair.


-----Output-----

Output "YES" if there exist two integers $x$ and $y$ ($1 \leq x < y \leq n$) such that in each given pair at least one integer is equal to $x$ or $y$. Otherwise, print "NO". You can print each letter in any case (upper or lower).


-----Examples-----
Input
4 6
1 2
1 3
1 4
2 3
2 4
3 4

Output
NO

Input
5 4
1 2
2 3
3 4
4 5

Output
YES

Input
300000 5
1 2
1 2
1 2
1 2
1 2

Output
YES



-----Note-----

In the first example, you can't choose any $x$, $y$ because for each such pair you can find a given pair where both numbers are different from chosen integers.

In the second example, you can choose $x=2$ and $y=4$.

In the third example, you can choose $x=1$ and $y=2$.
"""

def check_pairs_for_x_y(n, m, pairs):
    # Convert pairs to a list of sets for easier membership testing
    pair_sets = [set(pair) for pair in pairs]
    
    # Check each element in the first pair
    for e in pair_sets[0]:
        # Track if we find a valid x, y pair
        valid_x_y_found = True
        
        # Check each pair to see if e is in it
        for i in range(m):
            if e not in pair_sets[i]:
                # If e is not in the pair, check the other element in the pair
                for el in pair_sets[i]:
                    # Check if el is in all subsequent pairs
                    valid_el_found = True
                    for j in range(i, m):
                        if el not in pair_sets[j] and e not in pair_sets[j]:
                            valid_el_found = False
                            break
                    if valid_el_found:
                        break
                if not valid_el_found:
                    valid_x_y_found = False
                    break
        
        if valid_x_y_found:
            return "YES"
    
    return "NO"