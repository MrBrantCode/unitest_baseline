"""
QUESTION:
Chef has an array A consisting of N elements. He wants to find number of pairs of non-intersecting segments [a, b] and [c, d] (1 ≤ a ≤ b < c ≤ d ≤ N) such there is no number that occurs in the subarray {Aa, Aa+1, ... , Ab} and   {Ac, Ac+1, ... , Ad} simultaneously. 
Help Chef to find this number.

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains a single integer N denoting the number of elements in the array.
- The second line contains N space-separated integers A1, A2, ..., AN. 

-----Output-----
- For each test case, output a single line containing one integer - number of pairs of non-intersecting segments. 

-----Constraints-----
- 1 ≤ T ≤ 5
- 1 ≤ N ≤ 1000
- 1 ≤ Ai ≤ 109

-----Subtasks-----Subtask 1 (7 points)
- 1 ≤ N ≤ 20Subtask 2 (34 points)
- 1 ≤ N ≤ 300Subtask 3 (59 points)
- Original constraints

-----Example-----
Input:
2
3
1 2 3
4
1 2 1 2

Output:
5
4

-----Explanation-----
Example case 1.
All possible variants are correct: {[1, 1], [2, 2]}, {[1, 1], [2, 3]}, {[1, 2], [3, 3]}, {[2, 2], [3, 3]}, {[1,1], [3, 3]}.

Example case 2.
Correct segments: {[1, 1], [2, 2]}, {[1, 1], [4, 4]}, {[2, 2], [3, 3]}, {[3, 3], [4, 4]}.
"""

def count_non_intersecting_segments(test_cases):
    results = []
    
    for case in test_cases:
        N = case[0]
        A = case[1]
        
        if len(set(A)) == N:
            # If all elements are unique, use the formula for unique elements
            n = N + 2
            result = n * (n - 1) * (n - 2) * (n - 3) // 24
            results.append(result)
            continue
        
        counter = 0
        for i in range(N - 1):
            dic = {}
            for j in range(i, N - 1):
                if A[j] in dic:
                    dic[A[j]] += 1
                else:
                    dic[A[j]] = 1
                for p in range(j + 1, N):
                    if A[p] in dic:
                        continue
                    for q in range(p, N):
                        if A[q] in dic:
                            break
                        counter += 1
        
        results.append(counter)
    
    return results