"""
QUESTION:
Killgrave wants to use his mind control powers to get money from the Justice League superheroes living in $N$ houses in Happy Harbor that are numbered sequentially from $1$ to $N$. There are $\mbox{M}$ roads, and each road $j$ connects two different houses, $A_j$ and $B_j$. Each superhero house $\boldsymbol{i}$ (where $1\leq i\leq N$) has $C_i$ dollars stashed away for a rainy day.

As long as a superhero is home at house $\boldsymbol{i}$, Killgrave knows they will hand over all of their saved money, $C_i$. Once he gets money from them, he moves on to the next house. However, the superheroes are cunning; when Killgrave comes to house $\mbox{X}$, every neighbor immediately connected to house $\mbox{X}$ by a single road skips town for a couple of days (making it impossible for Killgrave to get money from them). In other words, after Killgrave visits all the superheroes he wants, there will be no road in which he was able to get money from both houses on either end of the road.

What is the maximum amount of money Killgrave can collect from the superheroes, and how many different ways can Killgrave get that amount of money? Two ways are considered to be different if the sets of visited houses are different.

Note: Killgrave can start at an arbitrary house and doesn't have to only use the roads.

Input Format

The first line contains two space-separated integers, $N$ (the number of houses) and $\mbox{M}$ (the number of roads), respectively. 

The second line contains $N$ space-separated integers, where each integer $\boldsymbol{i}$ describes the amount of money, $C_i$, at house $\boldsymbol{i}$. 

Each line $j$ of the $\mbox{M}$ subsequent lines contains two space-separated integers defining a road connecting houses $A_j$ and $B_j$. Every road connects a different pair of houses.

Constraints

$1\leq N\leq34$
$0\leq M\leq N\cdot\frac{(N-1)}{2}$
$0\leq C_i\leq100$
$1\leq A_j,B_j\leq N$, where $A_j\neq B_j$
No unordered pair $(A_j,B_j)$ will appear more than once.

Output Format

Print two space-separated integers:

The first integer must denote the maximum amount of money Killgrave can get out of the Justice League.
The second integer must denote the number of different ways he can collect that amount of money.

Sample Input
3 2
6 8 2
1 2
3 2

Sample Output
8 2

Explanation

Killgrave has two possible courses of action:

Visit house $2$ and get $8$ dollars.
Visit houses $1$ and $3$ and get $2+6=8$ dollars. 

Both of these options result in $8$ dollars, so we know that this is maximal. Thus, we print the maximum amount of money ($8$) followed by the number of ways he can get that amount of money ($2$) as two space-separated values on a single line.
"""

def calculate_max_money_ways(N, M, C, roads):
    # Create the adjacency list for the graph
    G = {a: set() for a in range(N)}
    for (a, b) in roads:
        G[a - 1].add(b - 1)
        G[b - 1].add(a - 1)
    
    minLost = {}

    def getMinLost(housesToVisit):
        if not housesToVisit:
            return (0, 1)
        key = frozenset(housesToVisit)
        if key in minLost:
            return minLost[key]
        a = housesToVisit.pop()
        (lost, nb) = getMinLost(housesToVisit)
        lost += C[a]
        lostHouses = set((b for b in G[a] if b in housesToVisit))
        lostMoney = sum((C[b] for b in lostHouses))
        (losta, nba) = getMinLost(housesToVisit - lostHouses)
        losta += lostMoney
        housesToVisit.add(a)
        if losta < lost:
            (lost, nb) = (losta, nba)
        elif losta == lost:
            nb += nba
        minLost[key] = (lost, nb)
        return minLost[key]
    
    (amount, number) = getMinLost(set(range(N)))
    return (sum(C) - amount, number)