"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

There are $N$ athletes (numbered $1$ through $N$) in a line. For each valid $i$, the $i$-th athlete starts at the position $i$ and his speed is $V_{i}$, i.e. for any real number $t ≥ 0$, the position of the $i$-th athlete at the time $t$ is $i + V_{i} \cdot t$.

Unfortunately, one of the athletes is infected with a virus at the time $t = 0$. This virus only spreads from an infected athlete to another whenever their positions are the same at the same time. A newly infected athlete may then infect others as well.

We do not know which athlete is infected initially. However, if we wait long enough, a specific set of athletes (depending on the athlete that was infected initially) will become infected. Your task is to find the size of this set, i.e. the final number of infected people, in the best and worst possible scenario.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
The second line contains $N$ space-separated integers $V_{1}, V_{2}, \ldots, V_{N}$.

------  Output ------
For each test case, print a single line containing two space-separated integers ― the smallest and largest final number of infected people.

------  Constraints ------
$1 ≤ T ≤ 10^{4}$
$3 ≤ N ≤ 5$
$0 ≤ V_{i} ≤ 5$ for each valid $i$

------  Subtasks ------
Subtask #1 (1 point): $N = 3$

Subtask #2 (99 points): original constraints

----- Sample Input 1 ------ 
4

3

1 2 3

3

3 2 1

3

0 0 0

3

1 3 2
----- Sample Output 1 ------ 
1 1

3 3

1 1

1 2
----- explanation 1 ------ 
Example case 1: No two athletes will ever have the same position, so the virus cannot spread.

Example case 2: It does not matter who is initially infected, the first athlete would always spread it to everyone.

Example case 3: The athletes are not moving, so the virus cannot spread.

Example case 4: The best possible scenario is when the initially infected athlete is the first one, since he cannot infect anyone else. In the worst possible scenario, eventually, the second and third athletes are infected.
"""

def calculate_infected_range(N, V):
    b, w = N, 1  # b: best scenario, w: worst scenario
    
    for i in range(N):
        a = [0] * N  # a: array to track infected athletes
        a[i] = 1  # assume athlete i is initially infected
        
        # Check left side of i
        for j in range(i):
            if V[j] > V[i]:
                a[j] = 1
        
        # Check right side of i
        for j in range(i + 1, N):
            if V[j] < V[i]:
                a[j] = 1
        
        # Propagate infection to the left
        for j in range(i):
            if a[j] == 1:
                for z in range(i, N):
                    if V[z] < V[j]:
                        a[z] = 1
        
        # Propagate infection to the right
        for j in range(i + 1, N):
            if a[j] == 1:
                for y in range(i):
                    if V[j] < V[y]:
                        a[y] = 1
        
        f = a.count(1)  # count the number of infected athletes
        w = max(f, w)  # update worst scenario
        b = min(f, b)  # update best scenario
    
    return b, w