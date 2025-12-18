"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

Chef has an array A = (A_{1}, A_{2}, ..., A_{N}), which has N integers in it initially. Chef found that for i ≥ 1, if A_{i} > 0, A_{i+1} > 0, and A_{i+2} exists, then he can decrease both A_{i}, and A_{i+1} by one and increase A_{i+2} by one. If A_{i+2} doesn't exist, but A_{i} > 0, and A_{i+1} > 0, then he can decrease both A_{i}, and A_{i+1} (which will be the currently last two elements of the array) by one and add a new element at the end, whose value is 1.

Now Chef wants to know the number of different arrays that he can make from A using this operation as many times as he wishes. Help him find this, and because the answer could be very large, he is fine with you reporting the answer modulo 10^{9}+7.

Two arrays are same if they have the same number of elements and if each corresponding element is the same. For example arrays (2,1,1) and (1,1,2) are different. 

------ Input ------ 

The first line of the input contains a single integer T denoting the number of test cases.
The first line contains a single integer N denoting the initial number of elements in A.
The second line contains N space-separated integers: A_{1}, A_{2}, ... , A_{N}. 

------ Output ------ 

For each test case, output answer modulo 10^{9}+7 in a single line. 

------ Constraints ------ 

$1 ≤ T ≤ 5$
$1 ≤ N ≤ 50$
$0 ≤ A_{i} ≤ 50$

------ Subtasks ------ 

$Subtask 1 (20 points) : 1 ≤ N ≤ 8, 0 ≤ A_{i} ≤ 4$
$Subtask 2 (80 points) : Original constraints$

------ Example ------ 

Input:
3
3
2 3 1
2
2 2
3
1 2 3

Output:
9
4
9

------ Explanation ------ 

Example case 1.
We'll list the various single steps that you can take (ie. in one single usage of the operation):

$(2, 3, 1) → (2, 2, 0, 1)$
$(2, 2, 0, 1) → (1, 1, 1, 1)$
$(1, 1, 1, 1) → (1, 1, 0, 0, 1)$
$(1, 1, 0, 0, 1) → (0, 0, 1, 0, 1)$
$(1, 1, 1, 1) → (1, 0, 0, 2)$
$(1, 1, 1, 1) → (0, 0, 2, 1)$
$(2, 3, 1) → (1, 2, 2)$
$(1, 2, 2) → (0, 1, 3)$

So all the arrays you can possibly get are: 
(2, 3, 1), (2, 2, 0, 1), (1, 1, 1, 1), (1, 1, 0, 0, 1), (0, 0, 1, 0, 1), (1, 0, 0, 2), (0, 0, 2, 1), (1, 2, 2), and (0, 1, 3)
Since there are 9 different arrays that you can reach, the answer is 9.
"""

MOD = 10 ** 9 + 7

def count_distinct_arrays(N, A):
    def process(p, num):
        (g, ln) = ({}, {})
        for (key, value) in p.items():
            (last1, next1) = (key[0], key[1] + num)
            if next1 not in ln:
                ln[next1] = [(last1, value)]
            else:
                ln[next1].append((last1, value))
            ln[next1].sort()
        for (next1, ln1) in ln.items():
            lns = sum((p[1] for p in ln[next1]))
            (lnp, lastm, next2, K) = (0, 0, 0, len(ln1))
            while lnp < K:
                nkey = (next1, next2)
                g[nkey] = (g.get(nkey, 0) + lns) % MOD
                while lnp < K and lastm >= ln1[lnp][0]:
                    lns -= ln1[lnp][1]
                    lnp += 1
                if next1 == 0:
                    break
                lastm += 1
                next1 -= 1
                next2 += 1
        return g
    
    p = {(0, 0): 1}
    for num in A:
        p = process(p, num)
    while len(p) > 1 or next(iter(p.keys())) != (0, 0):
        p = process(p, 0)
    
    return p[0, 0]