"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

------ Sereja and Arrays ------ 

Sereja have an array that consist of n integers a1, a2, ..., an (0 ≤ ai ≤ 1). Sereja can make next operation:  fix some integer i (1 ≤ i ≤ n - k + 1)  

subtract 1 from values: ai, ai + 1, ..., ai + k - 1Sereja call array a good if it is possible to make some operations, that he can and get array that contain only zeros. Now Sereja interested in next question: how many good arrays a with length n exist?

------ Input ------ 
First line contain integer T — number of testcases. T tests follow. Each testcase is given by two integers n and k.

------ Constraints ------ 
$ 1 ≤ T ≤ 10 $ $ 1 ≤ k ≤ n ≤ 105 $ 

------ Output ------ 
For each testcase output answer modulo 109 + 7.

------ Note ------ 

Test #0-1(25 points) n  ≤ 15
Test #2(25 points) n  ≤ 100
Test #3(50 points) n  ≤ 100000

----- Sample Input 1 ------ 
3
3 3
5 2
5 1
----- Sample Output 1 ------ 
2
8
32
"""

def count_good_arrays(T, test_cases):
    mod = 10 ** 9 + 7
    results = []
    
    for n, k in test_cases:
        if n == k:
            results.append(2)
            continue
        
        sm = [0] * n
        vals = [0] * n
        
        for i in range(n):
            if i < k:
                vals[i] = 1
            else:
                vals[i] = (sm[i - k] + 1) % mod
            
            if i != 0:
                sm[i] = (sm[i - 1] + vals[i]) % mod
            else:
                sm[i] = vals[i] % mod
        
        results.append((sm[-k] + 1) % mod)
    
    return results