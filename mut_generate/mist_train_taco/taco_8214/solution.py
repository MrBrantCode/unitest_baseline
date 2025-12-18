"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Jem couldn't even finish half of the homework exercises in "Advanced topics in algorithm" class. The teacher is really upset and gives him one final problem to solve - if he can't solve it, he is gonna fail the course.

Jem is given an array A consisting of N integers. The teacher asks him to remove exactly one number in the array to make the array become an arithmetic progressions.

Jem wanted to ask the teacher about the definition of arithmetic progressions but he remembered that he had heard this term in last week's lesson just before falling asleep. Now his life is in your hands again!

Anyways, we provide you the definition of arithmetic progression. Arithmetic progression is a sequence of numbers, where the difference between any two adjacent numbers is same.

------ Input ------ 

Input contains mutilpe test cases. The first line of the input contains a single integer T represents the number of tests. It is followed by T group of line represent the test cases.
Each test case consists of two lines where the first line contains a single integer N.
The second line contains N space separated integers denoting the array A.

------ Output ------ 

For each test case print out single integer which is the number you will remove from the array. If there is more than one solution take the smallest one. If there is no solution print out -1.

------ Constraints ------ 

$1 ≤ T ≤ 10 $
$2 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} ≤ 10^{9}$

----- Sample Input 1 ------ 
3
2
3 4
4
1 5 3 4
6
2 4 6 7 8 10
----- Sample Output 1 ------ 
3
-1
7
----- explanation 1 ------ 

test 1: an array contain a single integer is considered to be an arithmetic progression so you can remove any number in the array. But note that we must print out the smallest result which is 3.

test 2: there is no solution since none of [1, 3, 4], [1, 5, 3], [1, 5, 4], [5, 3, 4] is an arithmetic progressions.

test 3: the only way to archive an airthmetic progressions is remove the number 7 which will give us [2, 4, 6, 8, 10].
"""

from collections import defaultdict

def find_removal_for_arithmetic_progression(test_cases):
    results = []
    
    for N, A in test_cases:
        differences = defaultdict(lambda: 0)
        
        for i in range(1, N):
            differences[A[i] - A[i - 1]] += 1
        
        if len(differences) > 3:
            results.append(-1)
            continue
        
        ans = float('inf')
        
        for i in range(N):
            temp = differences.copy()
            
            if i > 0:
                temp[A[i] - A[i - 1]] -= 1
                if temp[A[i] - A[i - 1]] == 0:
                    del temp[A[i] - A[i - 1]]
            
            if i < N - 1:
                temp[A[i + 1] - A[i]] -= 1
                if temp[A[i + 1] - A[i]] == 0:
                    del temp[A[i + 1] - A[i]]
            
            if i != N - 1 and i != 0:
                temp[A[i + 1] - A[i - 1]] += 1
            
            if len(temp) <= 1:
                ans = min(ans, A[i])
        
        if ans != float('inf'):
            results.append(ans)
        else:
            results.append(-1)
    
    return results