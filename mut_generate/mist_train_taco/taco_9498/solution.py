"""
QUESTION:
Given an array A consisting of N integers A_{1},A_{2},…,A_{N}, determine if you can sort this array by applying the following operation several times (possibly, zero):
      
Pick a pair of indices (i,j) with i \neq j and A_{i} \mathbin{\&} A_{j} \neq 0, and swap the values of A_{i} and A_{j}. Here, \mathbin{\&} denotes the [bitwise AND operation].

For example, if A = [6, 4, 2], the two possible operations are (1, 2) and (1, 3). (2, 3) cannot be performed because A_{2} \mathbin{\&} A_{3} = 4 \mathbin{\&} 2 = 0.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N.
- The second line contains N space-separated integers A_{1}, A_{2}, \dots, A_{N}

------ Output Format ------ 

For each test case, output the answer on a new line — YES if the given array can be sorted by repeatedly applying the given operation, and NO otherwise.

You may print each character of the answer string in either uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 3 \cdot 10^{5}$
$0 ≤ A_{i} < 2^{31}$ for each $1 ≤ i ≤ N$
- The sum of $N$ over all test cases does not exceed $3 \cdot 10^{5}$

------ subtasks ------ 

Subtask #1 (100 points): Original constraints

----- Sample Input 1 ------ 
4
3
6 4 2
6
9 34 4 24 1 6
6
9 34 24 4 1 6
2
1 0
----- Sample Output 1 ------ 
Yes
Yes
No
No
----- explanation 1 ------ 
Test case $1$: $A$ can be sorted by applying the single operation $(1, 3)$.

Test case $2$: $A$ can be sorted by applying the following operations in order: $(1,5), (2,6), (2,3), (4,5)$.

Test cases $3$ and $4$: It can be shown that no sequence of operations will sort $A$.
"""

from collections import defaultdict

def can_sort_by_bitwise_swap(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        nums = A
        ans = True
        bitsets = defaultdict(set)
        bits_unified = defaultdict(set)
        
        for idx, num in enumerate(nums):
            matching_sets = []
            unified_or = num
            for bu in bits_unified:
                if bu & num > 0:
                    unified_or |= bu
                    matching_sets.append(bu)
            for match in matching_sets:
                del bits_unified[match]
            bits_unified[unified_or] = set()
            for i in range(32):
                if num & 1 << i:
                    bitsets[i].add(idx)
        
        for bu in bits_unified:
            for i in range(32):
                if bu & 1 << i:
                    bits_unified[bu] = bits_unified[bu].union(bitsets[i])
        
        for k in bits_unified:
            bitgroup = bits_unified[k]
            n = len(bitgroup)
            vals = sorted([nums[i] for i in bitgroup])
            indices = sorted([i for i in bitgroup])
            for i in range(n):
                nums[indices[i]] = vals[i]
        
        ans = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                ans = False
                break
        
        if ans:
            results.append("YES")
        else:
            results.append("NO")
    
    return results