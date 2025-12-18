"""
QUESTION:
Chef has an array A of length N.

In one operation, Chef can:
Choose any two distinct indices i, j (1≤ i, j≤ N) and change both A_{i} and A_{j} to (A_{i} + A_{j}). Note that both the elements A_{i} and A_{j} are getting replaced by the same value.

Find the minimum number of operations required by Chef to make all the elements divisible by 3.

It is guaranteed that we can make all the elements divisible by 3 using some finite number of operations.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N - denoting the length of array A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots A_{N}.

------ Output Format ------ 

For each test case, output the minimum number of operations required by Chef to make all the elements divisible by 3.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$4 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{5}$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
4
4 8 20 16
4
4 3 6 9

----- Sample Output 1 ------ 
2
6

----- explanation 1 ------ 
Test case $1$: We can make all the elements divisible by $3$ using $2$ operations.
- Operation $1$: Choose $i = 1$ and $j = 2$. Thus, we replace both $A_{1}$ and $A_{2}$ by $A_{1}+A_{2} = 4+8 = 12$. The array becomes $[12, 12, 20, 16]$.
- Operation $2$: Choose $i = 3$ and $j = 4$. Thus, we replace both $A_{3}$ and $A_{4}$ by $A_{3}+A_{4} = 20+16 = 36$. The array becomes $[12, 12, 36, 36]$.

All elements of the array are divisible by $3$. It can be shown that this is the minimum number of operations required to do so.

Test case $2$: We can make all the elements divisible by $3$ using $6$ operations.
- Operation $1$: Choose $i = 1$ and $j = 2$. Thus, we replace both $A_{1}$ and $A_{2}$ by $A_{1}+A_{2} = 4+3 = 7$. The array becomes $[7, 7, 6, 9]$.
- Operation $2$: Choose $i = 1$ and $j = 3$. Thus, we replace both $A_{1}$ and $A_{3}$ by $A_{1}+A_{3} = 7+6 = 13$. The array becomes $[13, 7, 13, 9]$.
- Operation $3$: Choose $i = 1$ and $j = 2$. Thus, we replace both $A_{1}$ and $A_{2}$ by $A_{1}+A_{2} = 13+7 = 20$. The array becomes $[20, 20, 13, 9]$.
- Operation $4$: Choose $i = 3$ and $j = 4$. Thus, we replace both $A_{3}$ and $A_{4}$ by $A_{3}+A_{4} = 13+9 = 22$. The array becomes $[20, 20, 22, 22]$.
- Operation $5$: Choose $i = 1$ and $j = 3$. Thus, we replace both $A_{1}$ and $A_{3}$ by $A_{1}+A_{3} = 20+22= 42$. The array becomes $[42, 20, 42, 22]$.
- Operation $6$: Choose $i = 2$ and $j = 4$. Thus, we replace both $A_{2}$ and $A_{4}$ by $A_{2}+A_{4} = 20+22= 42$. The array becomes $[42, 42, 42, 42]$.

All elements of the array are divisible by $3$. It can be shown that this is the minimum number of operations required to do so.
"""

def min_operations_to_make_divisible_by_3(arr):
    c0, c1, c2 = 0, 0, 0
    
    # Count the number of elements that are 0, 1, and 2 modulo 3
    for x in arr:
        if x % 3 == 0:
            c0 += 1
        elif x % 3 == 1:
            c1 += 1
        else:
            c2 += 1
    
    # Calculate the difference between c1 and c2
    diff = abs(c1 - c2)
    
    # Ensure c1 is the larger count
    if c2 > c1:
        c1, c2 = c2, c1
    
    res = 0
    
    # Determine the minimum number of operations based on the difference
    if diff == 0:
        res = c1
    elif diff == 1:
        if c2 == 0:
            res = 6
        else:
            res = c1 + 1
    elif diff == 2:
        if c2 == 0:
            res = 5
        elif c2 > 1:
            res = c1 + 2
        elif c2 == 1:
            if c0 == 0:
                res = 6
            else:
                res = 5
    elif diff == 3:
        res = c1 + 1
    elif diff == 4:
        res = c2 + 3
    else:
        res = (diff // 4 - 1) * 3
        diff = diff % 4
        res += c2 + 1
        if diff == 0:
            res += 2
        elif diff == 1:
            res += 4
        elif diff == 2:
            res += 6
        elif diff == 3:
            res += 6
    
    return res