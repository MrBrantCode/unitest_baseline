"""
QUESTION:
Chef loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Let F_{d}(x) equals to the number of digits d in decimal representation of the positive integer x. Chef interests only in functions F_{4}(x) and F_{7}(x). For the given positive integer N he wants to know the total number of different pairs (L; R) such that  F_{4}(L) + F_{4}(L + 1) + ... + F_{4}(R) equals to  F_{7}(L) + F_{7}(L + 1) + ... + F_{7}(R) and 1 ≤  L ≤ R ≤ N.

------ Input ------ 

The first line contains a single positive integer T, the number of test cases. T test cases follow. The only line of each test case contains a positive integer N .

------ Output ------ 

For each test case, output a single line containing the answer for the corresponding test case.

------ Constraints ------ 

1 ≤ T ≤ 100000

1 ≤ N ≤ 100000

----- Sample Input 1 ------ 
3
3
10
100
----- Sample Output 1 ------ 
6
31
1266
"""

def count_lucky_pairs(N):
    # Precompute the necessary values up to the maximum possible N
    n = 100000
    d = {0: 1}
    s4 = [0]
    s7 = [0]
    
    # Compute cumulative counts of '4' and '7' digits
    for i in range(1, n + 1):
        v = str(i)
        s4.append(s4[-1] + v.count('4'))
        s7.append(s7[-1] + v.count('7'))
    
    # Compute the difference between cumulative counts of '4' and '7'
    s4_7 = [0]
    for i in range(1, n + 1):
        s4_7.append(s4[i] - s7[i])
    
    # Compute the number of valid pairs for each prefix
    ans = [0]
    for i in range(1, n + 1):
        v = s4_7[i]
        if v in d:
            ans.append(ans[-1] + d[v])
            d[v] += 1
        else:
            ans.append(ans[-1])
            d[v] = 1
    
    # Return the precomputed result for the given N
    return ans[N]