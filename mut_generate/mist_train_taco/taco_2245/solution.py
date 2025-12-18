"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian  

Eugene has a sequence of upper hemispheres and another of lower hemispheres. The first set consists of N upper hemispheres indexed 1 to N and the second has M lower hemispheres indexed 1 to M. The hemispheres in any sequence can have different radii.
He is now set out on building spheres using them. To build a sphere of radius R, he must take one upper half of the radius R and one lower half of the radius R. Also, he can put a sphere into a bigger one and create a sequence of nested concentric spheres. But he can't put two or more spheres directly into another one.
Examples: 

If there is a sequence of (D+1) nested spheres, we can call this sequence as a D-sequence.

Eugene has to find out how many different X-sequence are possible (1 ≤ X ≤ C). An X sequence is different from another if the index of any of the hemisphere used in one X-sequence is different from the other. Eugene doesn't know how to do it, so Chef agreed to help him. Of course, Chef is too busy now and he asks you to help him.

------ Input ------ 

The first line contains a three integers: N denoting the number of upper sphere halves, M denoting the number of lower sphere halves and C.
The second line contains N space-separated integers U_{1}, U_{2}, ..., U_{N} denoting the radii of upper hemispheres.
The third line contains M space-separated integers L_{1}, L_{2}, ..., L_{M} denoting the radii of lower hemispheres.

------ Output ------ 

Output a single line containing C space-separated integers D_{1}, D_{2}, ..., D_{C}, where D_{i} is the number of ways there are to build i-sequence in modulo 10^{9}+7.

------ Constraints ------ 

$1 ≤ N ≤ 10^{5}$
$1 ≤ M ≤ 10^{5}$
$1 ≤ C ≤ 10^{3}$
$1 ≤ U_{i} ≤ C$
$1 ≤ L_{i} ≤ C$

------ Subtasks ------ 

$Subtask 1:  1 ≤ N, M, C ≤ 10 - 15 points$
$Subtask 2: 1 ≤ N, M, C ≤ 100 - 25 points$
$Subtask 3: Original constraints - 60 points$

----- Sample Input 1 ------ 
3 4 3
1 2 3
1 1 3 2
----- Sample Output 1 ------ 
5 2 0
----- explanation 1 ------ 

We can build spheres with such radii:
R=1 and there are 2 ways to do it. (We can choose any of 2 lower hemispheres with R=1)
R=2 and there is 1 way to do it.
R=3 and there is 1 way to do it.

We can build these 1-sequences:
1->2 and there are 2 ways to do it. ( sphere with radius 1 is inside sphere with radius 2, we can choose any of 2 ways of building sphere with radius 1)
1->3 and there are 2 ways to do it.
2->3 and there is 1 way to do it.

2 + 2 + 1 = 5

We can build these 2-sequences:
1->2->3 and there are 2 ways to do it.

We can't build 3-sequences, because we don't have 4 spheres of different radii.
"""

import collections

mod = 10 ** 9 + 7

def getsum(BITTree, i):
    s = 0
    i = i + 1
    while i > 0:
        s += BITTree[i]
        i -= i & -i
    return s

def updatebit(BITTree, n, i, v):
    i += 1
    while i <= n:
        BITTree[i] += v
        i += i & -i

def construct(arr, n):
    BITTree = [0] * (n + 1)
    for i in range(n):
        updatebit(BITTree, n, i, arr[i])
    return BITTree

def count_x_sequences(N, M, C, upper_radii, lower_radii):
    uh = collections.Counter(upper_radii)
    lh = collections.Counter(lower_radii)
    
    l = []
    for i in uh:
        if i in lh:
            l.append([i, uh[i] * lh[i]])
    l.sort()
    
    freq = [i[1] for i in l]
    n = len(freq)
    arr = [0] * n
    BITTree = construct(freq, n)
    
    result = []
    for i in range(1, C + 1):
        if i + 1 <= n:
            BITTreePresent = construct(arr, n)
            for j in range(i, n):
                updatebit(BITTreePresent, n, j, getsum(BITTree, j - 1) * freq[j] % mod)
            result.append(getsum(BITTreePresent, n - 1) % mod)
            BITTree = BITTreePresent
        else:
            result.append(0)
    
    return result