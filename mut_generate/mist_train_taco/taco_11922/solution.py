"""
QUESTION:
Stepan is a very experienced olympiad participant. He has n cups for Physics olympiads and m cups for Informatics olympiads. Each cup is characterized by two parameters — its significance c_{i} and width w_{i}.

Stepan decided to expose some of his cups on a shelf with width d in such a way, that:  there is at least one Physics cup and at least one Informatics cup on the shelf,  the total width of the exposed cups does not exceed d,  from each subjects (Physics and Informatics) some of the most significant cups are exposed (i. e. if a cup for some subject with significance x is exposed, then all the cups for this subject with significance greater than x must be exposed too). 

Your task is to determine the maximum possible total significance, which Stepan can get when he exposes cups on the shelf with width d, considering all the rules described above. The total significance is the sum of significances of all the exposed cups.


-----Input-----

The first line contains three integers n, m and d (1 ≤ n, m ≤ 100 000, 1 ≤ d ≤ 10^9) — the number of cups for Physics olympiads, the number of cups for Informatics olympiads and the width of the shelf.

Each of the following n lines contains two integers c_{i} and w_{i} (1 ≤ c_{i}, w_{i} ≤ 10^9) — significance and width of the i-th cup for Physics olympiads.

Each of the following m lines contains two integers c_{j} and w_{j} (1 ≤ c_{j}, w_{j} ≤ 10^9) — significance and width of the j-th cup for Informatics olympiads.


-----Output-----

Print the maximum possible total significance, which Stepan can get exposing cups on the shelf with width d, considering all the rules described in the statement.

If there is no way to expose cups on the shelf, then print 0.


-----Examples-----
Input
3 1 8
4 2
5 5
4 2
3 2

Output
8

Input
4 3 12
3 4
2 4
3 5
3 4
3 5
5 2
3 4

Output
11

Input
2 2 2
5 3
6 3
4 2
8 1

Output
0



-----Note-----

In the first example Stepan has only one Informatics cup which must be exposed on the shelf. Its significance equals 3 and width equals 2, so after Stepan exposes it, the width of free space on the shelf becomes equal to 6. Also, Stepan must expose the second Physics cup (which has width 5), because it is the most significant cup for Physics (its significance equals 5). After that Stepan can not expose more cups on the shelf, because there is no enough free space. Thus, the maximum total significance of exposed cups equals to 8.
"""

def maximize_total_significance(n, m, d, physics_cups, informatics_cups):
    # Convert widths to negative to facilitate sorting by significance first, then by width
    for i in range(n):
        physics_cups[i][1] = -physics_cups[i][1]
    for i in range(m):
        informatics_cups[i][1] = -informatics_cups[i][1]
    
    # Sort cups by significance in descending order, then by width in ascending order
    physics_cups.sort(reverse=True)
    informatics_cups.sort(reverse=True)
    
    # Initialize variables
    total_significance = 0
    total_width = 0
    
    # Add all informatics cups to the shelf
    for cup in informatics_cups:
        total_significance += cup[0]
        total_width -= cup[1]  # Subtract because widths are negative
    
    # Initialize answer
    max_significance = 0
    z = m - 1
    
    # Try adding physics cups to the shelf
    for cup in physics_cups:
        total_significance += cup[0]
        total_width -= cup[1]  # Subtract because widths are negative
        
        # Remove the least significant informatics cup if the width exceeds the shelf's capacity
        while z >= 0 and total_width > d:
            total_significance -= informatics_cups[z][0]
            total_width += informatics_cups[z][1]  # Add because widths are negative
            z -= 1
        
        # If the current configuration fits within the shelf's width, update the maximum significance
        if total_width <= d:
            max_significance = max(max_significance, total_significance)
    
    return max_significance