"""
QUESTION:
、Consider an inifite array, $a$, of positive numbers, $a_1,a_2,\ldots$, where each $a_i=i$. You can apply a permutation, ${p}$, of size $n$ (i.e., $n$ different numbers $1\leq p_1,\ldots,p_n\leq n$) to the $n$-element subset of your array from $a_1$ through $a_n$ in the following way:  

$(a_1,...,a_n)\rightarrow(a_{p_1},...,a_{p_n}).$ 

To get infinite array ${b}$, you must apply permutation ${p}$ to the first $n$ elements ($a_1$ to $a_n$), then to elements $a_2$ through ${a_{n+1}}$, then to elements $a_3$ through $a_{n+2}$, and so on, infinitely many times. 

Given the values of $n$, $m$, and ${p}$, find and print the value of $b_m$. See the Explanation section below for more detail. 

Note: This challenge uses $1$-based array indexing.

Input Format

The first line contains $2$ space-separated integers, $n$ and $m$, respectively. 

The second line contains $n$ space-separated integers describing the respective values of $p_1,p_2,\ldots,p_n$.

Constraints

$1\leq n\leq10^5$
$1\leq m\leq10^{18}$  
$1\leq p_1,p_2,\ldots,p_n\leq n$, and each $p_i$ is unique.  

Output Format

Print a single integer denoting the value of $b_m$.

Sample Input 0

2 10
2 1

Sample Output 0

11

Sample Input 1

3 1
2 3 1

Sample Output 1

2

Sample Input 2

3 10
2 3 1

Sample Output 2

10 

Explanation

Sample Case 0 has the following sequence of array transformations: 

$\mathbf{1}\:\mathbf{2}\:3\:4\:5\:6\:7\:8\:9\:10\:11\:12\ldots$ 

${2}\:\mathbf{1}\:\mathbf{3}\:4\:5\:6\:7\:8\:9\:10\:11\:12\ldots$ 

${2\:3}\:\mathbf{1}\:\mathbf{4}\:{5}\:{6}\:{7}\:{8}\:{9}\:{10}\:{11}\:{12}\ldots$ 

${2\:3}\:4\:\mathbf{1}\:\mathbf5\:{6}\:7\:8\:9\:\:{10}\:11\:{12}...$ 

${2\:3}\:4\:5\:\mathbf1\:6\:7\:8\:9\:10\:11\:12\ldots$ 

${2\:3\:4\:5\:6}\:\mathbf{1}\:\mathbf7\:{8}\:{9}\:{10}\:{11}\:{12}\ldots$ 

${2\:3\:4\:5}\:{67}\:\mathbf{1\:8}\:{9}\:{10}\:{11}\:{12}\ldots$ 

${2\:3}\:4\:5\:6\:7\:8\:\mathbf{1\:9}\:10\:11\:12\ldots$ 

${2\:3\:4\:5}\:6\:7\:8\:9\:\mathbf{1}\:\mathbf10\:11\:12\ldots$ 

$2\:3\:4\:5\:6\:7\:89\:10\:\mathbf{1}\:\mathbf{11}\:12\ldots$ 

${2\:3}\:4\:5\:6\:7\:8\:9\:10\:11\:\mathbf{1}\:\mathbf{12}\:\ldots$   

As you can see, each $b_i=a_i+1=i+1$. Thus, we know that $b_m=m+1=10+1=11$.

Sample Case 1 and Sample Case 2 have the following sequence of array transformations: 

$\mathbf{1}\:\mathbf{2}\:\mathbf{3}\:{4}\:5\:{6}\:{7}\:{8}\:{9}\:{10}\:{11}\:{12}\:{13}\ldots$ 

${2}\:\mathbf{3}\:\mathbf{1\:4}\:5\:6\:7\:8\:9\:10\:11\:12\:13\ldots$ 

${2}\:{1}\:\mathbf4\:\mathbf{3}\:\mathbf5\:6\:{7}\:{8}\:{9}\:{10}\:{11}\:{12}\:{13}\ldots$ 

$2\:1\:3\:\mathbf{5}\:\mathbf{4}\:\mathbf{6}\:{7}\:{8}\:{9}\:{10}\:{11}\:{12}\:{13}\ldots$ 

${2}\:1\:3\:4\:\mathbf6\:\mathbf5\:\mathbf7\:8\:9\:10\:11\:12\:13\ldots$ 

$2\:1\:3\:4\:5\:\mathbf{7}\:\mathbf{6\:8}\:{9}\:{10}\:{11}\:{12}\:{13}\ldots$ 

${2}\:1\:3\:45\:6\:\mathbf8\:\mathbf{7\:9}\:10\:11\:12\:13\ldots$ 

${2}\:{1}\:{3}\:{4}\:{5}\:{6}\:{7}\:\mathbf{9}\:\mathbf{8}\:\mathbf{10}\:{11}\:{12}\:13}\ldots$ 

${2}\:{1}\:{3}\:4\:5\:{6}\:{7}\:{8}\:\mathbf{10}\:\mathbf{9}\:\mathbf{11}\:12\:13}\ldots$ 

${2}\:1\:3\:45\:6\:7\:89\:\mathbf{11}\:\mathbf{10}\:\mathbf{12}\:13\ldots$ 

${2\:1\:3}\:4\:5\:6\:7\:89\:10\:\mathbf{12}\:\mathbf{11}\:\mathbf{13}\:\ldots$        

As you can see, $b_1=2$ and $b_{10}=10$.
"""

def find_b_m(n, m, p):
    # Convert permutation indices to 0-based for easier manipulation
    p = list(map(lambda x: x - 1, p))
    
    # Initialize the order list to store the cycle
    order = []
    idx = n - 1
    
    # Traverse the permutation to find the cycle
    while p[idx] != -1:
        order.append(p[idx])
        tmp = p[idx]
        p[idx] = -1
        idx = tmp
    
    # Determine the value of b_m based on the cycle length
    if m > len(order):
        return m + (n - len(order))
    else:
        return order[m - 1] + 1