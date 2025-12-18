"""
QUESTION:
Vova has won $n$ trophies in different competitions. Each trophy is either golden or silver. The trophies are arranged in a row.

The beauty of the arrangement is the length of the longest subsegment consisting of golden trophies. Vova wants to swap two trophies (not necessarily adjacent ones) to make the arrangement as beautiful as possible — that means, to maximize the length of the longest such subsegment.

Help Vova! Tell him the maximum possible beauty of the arrangement if he is allowed to do at most one swap.


-----Input-----

The first line contains one integer $n$ ($2 \le n \le 10^5$) — the number of trophies.

The second line contains $n$ characters, each of them is either G or S. If the $i$-th character is G, then the $i$-th trophy is a golden one, otherwise it's a silver trophy. 


-----Output-----

Print the maximum possible length of a subsegment of golden trophies, if Vova is allowed to do at most one swap.


-----Examples-----
Input
10
GGGSGGGSGG

Output
7

Input
4
GGGG

Output
4

Input
3
SSS

Output
0



-----Note-----

In the first example Vova has to swap trophies with indices $4$ and $10$. Thus he will obtain the sequence "GGGGGGGSGS", the length of the longest subsegment of golden trophies is $7$. 

In the second example Vova can make no swaps at all. The length of the longest subsegment of golden trophies in the sequence is $4$. 

In the third example Vova cannot do anything to make the length of the longest subsegment of golden trophies in the sequence greater than $0$.
"""

def maximize_golden_trophies_beauty(n: int, trophies: str) -> int:
    a = []
    k = 1
    
    # Identify segments of consecutive 'G's
    for i in range(n - 1):
        if trophies[i] == 'G' and trophies[i + 1] == 'G':
            k += 1
        elif trophies[i] == 'G' and trophies[i + 1] == 'S':
            a.append([i, k])
            k = 1
    
    # Handle the last trophy
    if trophies[-1] == 'G':
        a.append([n - 1, k])
    
    # If there are no golden trophies
    if len(a) == 0:
        return 0
    
    # If there is only one segment of golden trophies
    elif len(a) == 1:
        return a[0][1]
    
    # If there are two segments of golden trophies
    elif len(a) == 2:
        ma = max(a[0][1], a[1][1])
        ka = 0
        if a[1][0] - a[1][1] + 1 - a[0][0] == 2:
            ka = a[0][1] + a[1][1]
        return max(ka, ma + 1)
    
    # If there are more than two segments of golden trophies
    else:
        ma = max(segment[1] for segment in a)
        ka = 0
        for i in range(len(a) - 1):
            if a[i + 1][0] - a[i + 1][1] + 1 - a[i][0] == 2:
                ka = max(a[i][1] + a[i + 1][1], ka)
        return max(ka, ma) + 1