"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

You are given a sequence a_{1}, a_{2}, ..., a_{N}. Count the number of triples (i, j, k) such that 1 ≤ i < j < k ≤ N and GCD(a_{i}, a_{j}, a_{k}) = 1. Here GCD stands for the Greatest Common Divisor.

------ Input ------ 

The first line of input contains a single integer N - the length of the sequence.

The second line contains N space-separated integers - a_{1}, a_{2}, ..., a_{N} respectively.

------ Output ------ 

Output the required number of triples on the first line of the output.

------ Constraints ------ 

$1 ≤ N ≤ 100 : 22 points.$
$1 ≤ N ≤ 1000 : 23 points.$
$1 ≤ N ≤ 10^{5} : 55 points.$
$1 ≤ a_{i} ≤ 10^{6}$

------ Example ------ 

Input:
4
1 2 3 4

Output:
4

------ Explanation ------ 

Any triple will be a coprime one.
"""

def count_coprime_triples(n, l):
    MA = max(l)
    count = [0] * (MA + 1)
    
    for i in l:
        count[i] += 1
    
    for i in range(1, MA + 1):
        for j in range(2 * i, MA + 1, i):
            count[i] += count[j]
        count[i] = count[i] * (count[i] - 1) * (count[i] - 2) // 6
    
    for i in range(MA, 0, -1):
        for j in range(2 * i, MA + 1, i):
            count[i] -= count[j]
    
    return count[1]