"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Sereja has a string A consisting of n lower case English letters. 

Sereja calls two strings X and Y each of length n similar if they can be made equal by applying the following operation at most once in each of them.

Chose any two position i, j in the string (i can be equal to j too). Swap the characters at position i with character at position j.

For example strings "abcd" and "acbd" are similar, strings "ab" and "ab" are similar, but strings "abcde" and "bcdea" are not similar. Note that strings  "abc" and "cab" are also similar, as you can swap 'a' and 'c' in the first string to get "cba" and 'a' and 'b' in the second string to get "cba". 

Now Sereja is interested in finding number of ordered pairs of non similar strings X and Y such that they can be constructed from a given string A by permutation of its characters. As answer could be large, please output your answer modulo  (10^{9} + 7).

Note 
A string s (of size n) is said to be constructed from string t (also of size n) by permutation of its characters if there exists a permutation P (of length n), such that s[i] = t[P[i]] for each i from 1 to n.

------ Input ------ 

First line contain integer T - number of test cases. 
For each of the next T lines: 
	
		Each line contains a string A as defined in the problem.
	
------ Output ------ 

For each test case, output answer modulo 1000000007 (10^{9} + 7) in separate line. 

------ Constraints ------ 

1 ≤ T ≤  10 
1 ≤ n ≤  10^{5} 

------ Constraints ------ 

Subtask #1: 1 ≤ n ≤  10  (25 points)
Subtask #2: 1 ≤ n ≤  100  (25 points)
Subtask #3: 1 ≤ n ≤  1000  (25 points)
Subtask #4: original constraints (25 points)

------ Example ------ 

Input:
2
z
abcd

Output:
0
144
"""

def count_non_similar_pairs(test_cases, fact, md):
    results = []
    
    for s in test_cases:
        counts = [s.count(x) for x in set(s)]
        sym4 = 0
        sym3 = 0
        sym2 = 0
        sym1 = 0
        sym1choose2 = 0
        sym2choose2 = 0
        sym1cchoose2 = 0
        sym1c2choose2 = 0
        choose_all = fact[len(s)]
        
        for c in counts:
            choose2 = c * (c - 1) // 2
            sym4 += sym3 * c
            sym3 += sym2 * c
            sym2 += sym1 * c
            sym1 += c
            sym2choose2 += sym1choose2 * choose2
            sym1choose2 += choose2
            sym1cchoose2 += c * choose2
            sym1c2choose2 += c * c * choose2
            choose_all *= pow(fact[c], -1, md)
            choose_all %= md
        
        num_swap = sym2
        num_3_cycle = 2 * sym3
        num_2_swaps_abcd = 3 * sym4
        num_2_swaps_aabc = 2 * (sym1choose2 * sym2 - sym1cchoose2 * sym1 + sym1c2choose2)
        num_2_swaps_aabb = sym2choose2
        num_sim = 1 + num_swap + num_3_cycle + num_2_swaps_aabb + num_2_swaps_aabc + num_2_swaps_abcd
        num_sim %= md
        
        ans = choose_all * (choose_all - num_sim)
        ans %= md
        
        results.append(ans)
    
    return results