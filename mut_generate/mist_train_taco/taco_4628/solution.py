"""
QUESTION:
Victoria is splurging on expensive accessories at her favorite stores. Each store stocks $\mbox{A}$ types of accessories, where the $i^{\mbox{th}}$ accessory costs $\boldsymbol{i}$ dollars ($1\leq i\leq A$). Assume that an item's type identifier is the same as its cost, and the store has an unlimited supply of each accessory.

Victoria wants to purchase a total of $L$ accessories according to the following rule:

Any $N$-element subset of the purchased items must contain at least $\mbox{D}$ different types of accessories. 

For example, if $L=6$, $N=3$, and $D=2$, then she must choose $\boldsymbol{6}$ accessories such that any subset of $3$ of the $\boldsymbol{6}$ accessories will contain at least $2$ distinct types of items. 

Given $L$, $\mbox{A}$, $N$, and $\mbox{D}$ values for $\mathbf{T}$ shopping trips, find and print the maximum amount of money that Victoria can spend during each trip; if it's not possible for Victoria to make a purchase during a certain trip, print SAD instead. You must print your answer for each trip on a new line.

Input Format

The first line contains an integer, $\mathbf{T}$, denoting the number of shopping trips. 

Each of the $\mathbf{T}$ subsequent lines describes a single shopping trip as four space-separated integers corresponding to $L$, $\mbox{A}$, $N$, and $\mbox{D}$, respectively.

Constraints

$1\leq T\leq10^6$  
$1\leq D\leq N\leq L\leq10^5$  
$1\leq A\leq10^9$  
The sum of the $L$'s for all $\mathbf{T}$ shopping trips $\leq8\cdot10^{6}$.  

Output Format

For each shopping trip, print a single line containing either the maximum amount of money Victoria can spend; if there is no collection of items satisfying her shopping rule for the trip's $L$, $\mbox{A}$, $N$, and $\mbox{D}$ values, print SAD instead.

Sample Input
2
6 5 3 2
2 1 2 2

Sample Output
24
SAD

Explanation

Shopping Trip 1: 

We know that:

Victoria wants to buy $L=6$ accessories. 
The store stocks the following $A=5$ types of accessories: $\{1,2,3,4,5\}$. 
For any grouping of $N=3$ of her $L$ accessories, there must be at least $D=2$ distinct types of accessories.  

Victoria can satisfy her shopping rule and spend the maximum amount of money by purchasing the following set of accessories: $\{3,4,5,5,4,3\}$. The total cost is $3+4+5+5+4+3=24$, so we print $24$ on a new line.

Shopping Trip 2: 

We know that:

Victoria wants to buy $L=2$ accessories.
The store stocks $A=1$ type of accessory: $\{1\}$. 
For any grouping of $N=2$ of her $L$ accessories, there must be at least $D=2$ distinct types of accessories. 

Because the store only carries $1$ type of accessory, Victoria cannot make a purchase satisfying the constraint that there be at least $D=2$ distinct types of accessories. Because Victoria will not purchase anything, we print that she is SAD on a new line.
"""

import math

def calculate_max_spending(L, A, N, D):
    def total(g):
        if g <= 0:
            return 0
        first = N - g * (D - 2) - 1
        f = (L - first) // g
        if first < g or A - f <= 0 or first + g * (A - 1) < L:
            return 0
        partial = int((2 * (A - 1) - f + 1) / 2 * f)
        left = (A - f - 1) * (-f * g + L - first)
        return first * A + partial * g + left

    if D == 1:
        return L * A
    
    if D == 2:
        n1 = N - 1
        if n1 * A >= L:
            ln1 = L // n1
            return int((2 * A + 1 - ln1) / 2 * ln1 * n1) + (A - ln1) * (L - ln1 * n1)
        else:
            return 'SAD'
    
    if A == 1:
        return 'SAD'
    
    if A == 2:
        if D == 2 and (N - D + 1) * 2 >= L:
            return N - D + L + 1
        else:
            return 'SAD'
    
    g = math.ceil((L - A - N + D) / (A - 2))
    if g > N - D:
        return 'SAD'
    
    argmax = int(math.sqrt((2 - 3 * D + D * D) * (1 + L - N) * (1 + L - N)) / (2 - 3 * D + D * D)) + 1
    if (D == 3 or (D == 4 and A > 2)) or (D > 4 and A > D - 2):
        argmax = max(int((1 + L - N) / (2 + A - D)), argmax)
        argmax = min(int((N - 1) / (D - 1)), argmax)
        if D == 3 or A > D - 1:
            argmax = max(int((1 + L - N) / (1 + A - D)), argmax)
        elif D > 3 and A < D - 1:
            argmax = min(int((1 + L - N) / (1 + A - D)), argmax)
    
    max_haul = max(total(argmax - 1), total(argmax), total(argmax + 1))
    return max_haul if max_haul else 'SAD'