"""
QUESTION:
Tara was completing an Algorithms assignment and got stuck on a question. She thought of who can help her, and got reminded of Kabir who has good problem solving skills. The question is:
Given N$N$ the number of elements in the sequence A1$A_1$,A2$A_2$ … An$A_n$. Find out the prime factor which occurred maximum number of times among the largest prime factor corresponding to each element. if there are more than one such prime factors print the largest one.
You are friends with Kabir, help him to solve the problem for Tara.

-----Input:-----
- The first line of the input contains a single integer T$T$ denoting the number of test cases. The description of T test cases follows. 
- First line of each test case contains N$N$, the number of elements in the sequence.
- Second line contains N space separated elements A1$A_1$,A2$A_2$ … An$A_n$.

-----Output:-----
- For each test case, print a single line, the number which occurs maximum number of times from the largest prime factor corresponding to each element.

-----Constraints-----
- 1≤T≤10$1 \leq T \leq 10$
- 1≤N≤105$1 \leq N \leq 10^5$
- 2≤A[i]≤105$2 \leq A[i] \leq 10^5$

-----Sample Input:-----
1
7

3 2 15 6 8 5 10

-----Sample Output:-----
5

-----EXPLANATION:-----
The largest prime factors of numbers are:
3 2  5  3  2  5  5 , of which 5 is most frequent.
"""

def find_most_frequent_largest_prime_factor(test_cases):
    # Precompute the largest prime factors for all numbers up to 10^5
    store = [0] * (10 ** 5 + 1)
    
    def sieve():
        for i in range(2, 10 ** 5 + 1):
            if store[i] == 0:
                store[i] = 1
                for j in range(i, 10 ** 5 + 1, i):
                    store[j] = i
    
    sieve()
    
    results = []
    
    for test_case in test_cases:
        N, sequence = test_case
        dp = [0] * (10 ** 5 + 1)
        
        # Count the occurrences of each largest prime factor
        for num in sequence:
            dp[store[num]] += 1
        
        max_re = 0
        res = 0
        
        # Find the most frequent largest prime factor
        for num in sequence:
            if dp[store[num]] == max_re:
                if store[num] > res:
                    res = store[num]
            elif dp[store[num]] > max_re:
                max_re = dp[store[num]]
                res = store[num]
        
        results.append(res)
    
    return results