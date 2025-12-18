"""
QUESTION:
D: Two Colors Sort

problem

During the walk, umg found a sequence of length N, P_1, P_2, ..., P_N, which can be made by rearranging 1,2, ..., N.

umg can use mysterious powers to exchange places by choosing two different numbers painted in the same color.

umg wanted to be able to sort the sequence in ascending order by painting R of the numbers in the sequence in red and the remaining N-R in blue.

umg Determine if you can reach your goal.

However, the numbers are so heavy that they cannot be moved without mysterious force. Also, since umg is a genius, you can use mysterious powers any number of times.

Input format


N R
P_1 P_2 ... P_N


Constraint

* 1 \ leq N \ leq 3 \ times 10 ^ 5
* 1 \ leq R \ leq N
* 1 \ leq P_i \ leq N
* P_i \ neq P_j (1 \ leq i <j \ leq N)
* All inputs are integers.



Output format

umg Print `Yes` if you can achieve your goal, otherwise` No` on one line.

Input example 1


3 2
1 3 2


Output example 1


Yes

* You can achieve your goal by painting 1 in blue and 2 and 3 in red.



Input example 2


5 2
1 2 3 4 5


Output example 2


Yes

* They are arranged in ascending order from the beginning.



Input example 3


10 7
3 4 8 5 7 6 2 10 1 9


Output example 3


No





Example

Input

3 2
1 3 2


Output

Yes
"""

def can_sort_sequence(N, R, P):
    if 2 * R > N:
        R = N - R
    
    P = [0] + P  # Adjust P to start from index 1 for easier indexing
    L = []
    used = [False] * (N + 1)
    pre = 0
    
    for i in range(1, N + 1):
        cnt = 0
        while not used[i]:
            used[i] = True
            cnt += 1
            i = P[i]
        if cnt:
            L.append(cnt)
    
    table = [0] * (N + 1)
    for l in L:
        table[l] += 1
    
    L = []
    for i in range(N // 2, 0, -1):
        x = table[i]
        if not x:
            continue
        if x == 1:
            L.append(i)
        else:
            p = 1
            while p + p <= x:
                L.append(p * i)
                p = p + p
            if x - p + 1:
                L.append(i * (x - p + 1))
    
    L = [l for l in L if l <= R]
    L.sort()
    
    H = 1
    for l in L:
        H = H | H << l
    
    if H & 1 << R:
        return 'Yes'
    else:
        return 'No'