"""
QUESTION:
Keko has $N$ dots in a 2-D coordinate plane. He wants to measure the gap between the most distant two dots. To make the problem easier, Keko decided to change each dot's $\boldsymbol{x}$ or $y$ coordinate to zero.   

Help Keko calculate the distance!

Input Format

The first line contains an integer, $N$, the number of dots. 

The next $N$ lines each contain the integer coordinates of the dots in $(x,y)$ fashion.  

Constraints 

$2\leq N\leq10^6$ 

$-10^9\leq x_i,\ y_i\leq10^9$

It is guaranteed that all dots are distinct, and either their $\boldsymbol{x}$ or $y$ coordinate is equal to $0$.  

Output Format

Print the distance between the most distant dots with an absolute error of, at most, $\mathbf{10^{-6}}$.

Sample Input
4
-1 0
1 0
0 1
0 -1

Sample Output
2.000000

Explanation

In the sample, the most distant dots are located at $(-1,0)$ and $(1,0)$. 

The distance between them is $2$.
"""

def calculate_max_distance(dots):
    xs = []
    ys = []
    
    for x, y in dots:
        if y == 0:
            xs.append(x)
        else:
            ys.append(y)
    
    xs.sort()
    ys.sort()
    
    max_distance_squared = 0
    
    if xs:
        max_distance_squared = max(max_distance_squared, (xs[-1] - xs[0]) ** 2)
    if ys:
        max_distance_squared = max(max_distance_squared, (ys[-1] - ys[0]) ** 2)
    if xs and ys:
        xx = max(abs(v) for v in xs)
        yy = max(abs(v) for v in ys)
        max_distance_squared = max(max_distance_squared, xx ** 2 + yy ** 2)
    
    return max_distance_squared ** 0.5