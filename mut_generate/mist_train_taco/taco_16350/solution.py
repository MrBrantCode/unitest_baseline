"""
QUESTION:
Given $\mbox{1}$ friendly number and $n$ unfriendly numbers, determine how many numbers are divisors of the friendly number but not the unfriendly numbers.

Input Format

The first line contains $2$ space-separated integers, $n$ (the number of unfriendly numbers) and $\mbox{f}$ (the friendly number), respectively. 
The second line contains $n$ space-separated unfriendly numbers.

Constraints

$1\leq n\leq10^{6}$
$1\leq f\leq10^{13}$
$1\leq\textit{unfriendly numbers}\leq10^{18}$

Output Format

Print the the number of unique divisors of $\mbox{f}$ (i.e.: divisors that are not shared with those of the unfriendly numbers) as a single integer.

Sample Input
8 16
2 5 7 4 3 8 3 18

Sample Output
1

Explanation

There are $n=8$ unfriendly numbers: $2,5,7,4,3,8,3,18$. 

Our friendly number, $\mbox{f}$, is $\mbox{16}$, and its even divisors are $1,2,4,8,16$. 

Let $\textit{count}$ be the number of friendly divisors that are not also unfriendly divisors. Let's determine which divisors of $\mbox{f}$ are not also divisors of the unfriendly numbers:

$\mbox{1}$ is a divisor of all unfriendly numbers, so we disregard it.   
$2$ is a divisor of unfriendly numbers $2$, $\begin{array}{c}4\end{array}$, and $8$, so we disregard it.
$\begin{array}{c}4\end{array}$ is a divisor of unfriendly numbers $\begin{array}{c}4\end{array}$ and $8$, so we disregard it.
$8$ is a divisor of unfriendly number $8$, so we disregard it. 
$\mbox{16}$ is not a divisor of any unfriendly number, so we increment $\textit{count}$ to $\mbox{1}$.

As there are no more friendly divisors to check, we print the value of $\textit{count}$ (which is $\mbox{1}$) on a new line.
"""

from math import gcd

def count_unique_friendly_divisors(n, f, unfriendly_numbers):
    # Find all divisors of the friendly number f
    divs = []
    for i in range(1, int(f ** 0.5) + 1):
        if f % i == 0:
            divs.append(i)
            if i != f // i:
                divs.append(f // i)
    
    # Find the unique gcds of f with each unfriendly number
    ndivs = set()
    for u in unfriendly_numbers:
        ndivs.add(gcd(f, u))
    
    # Count unique friendly divisors that are not in ndivs
    rt = 0
    for d in divs:
        for nd in ndivs:
            if nd % d == 0:
                break
        else:
            rt += 1
    
    return rt