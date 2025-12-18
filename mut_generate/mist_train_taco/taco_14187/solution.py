"""
QUESTION:
You are given an array A consisting of 2 \cdot N integers.

You can perform the following operation any number of times.
Choose any i (1 ≤ i ≤ 2 \cdot N) such that A_{i} is even and divide A_{i} by 2.
Or choose any i (1 ≤ i ≤ 2 \cdot N) and multiply A_{i} by 2.

Find the minimum number of operations required to make the number of even elements and number of odd elements in the array equal.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N — the size of the array A is 2 \cdot N.
- The second line of each test case contains 2 \cdot N space-separated integers A_{1}, A_{2}, \dots, A_{2 \cdot N} denoting the array A.

------ Output Format ------ 

For each test case, output on a new line the minimum number of operations required to make the number of even elements and number of odd elements in the array equal.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases is at most $10^{5}$.

----- Sample Input 1 ------ 
3
3
1 2 3 4 5 6
3
1 3 4 8 2 6
3
1 5 3 5 6 7

----- Sample Output 1 ------ 
0
1
2
----- explanation 1 ------ 
Test case 1: No operations are required since there are already an equal number of odd elements and even elements.       

Test case 2: One operation is enough. It can be seen that the number of odd and even elements in the resulting array are equal.

$[1, 3, 4, 8, \underline{2}, 6] \xrightarrow[\div 2]{i = 5} [1, 3, 4, 8, 1, 6]$

Test case 3: Here two operations are enough to make the number of odd and even elements in the resulting array equal.

1st operation: $[ 1, 5, 3,\underline{5}, 6, 7] \xrightarrow[\times 2 ]{i = 4} [1, 5, 3, 10, 6, 7]$
    
2nd operation: $[ 1, 5, 3, 10, 6, \underline{7}] \xrightarrow[\times 2 ]{i = 6} [1, 5, 3, 10, 6, 14]$
"""

def min_operations_to_balance_even_odd(test_cases):
    def pow(c):
        count = 0
        while c % 2 == 0:
            c = c // 2
            count += 1
        return count
    
    results = []
    
    for n, a in test_cases:
        e = 0
        o = 0
        ev = []
        
        for i in a:
            if i % 2 == 0:
                e += 1
                ev.append(i)
            else:
                o += 1
        
        if o == e:
            results.append(0)
        elif o > e:
            results.append((o - e) // 2)
        else:
            l = []
            for i in range(e):
                l.append(pow(ev[i]))
            l = sorted(l)
            d = (e - o) // 2
            b = l[:d]
            results.append(sum(b))
    
    return results