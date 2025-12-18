"""
QUESTION:
Chef likes toys. His favourite toy is an array of length N. This array contains only integers. He plays with this array every day. His favourite game with this array is Segment Multiplication. In this game, the second player tells the left and right side of a segment and some modulo. The first player should find the multiplication of all the integers in this segment of the array modulo the given modulus. Chef is playing this game. Of course, he is the first player and wants to win all the games. To win any game he should write the correct answer for each segment. Although Chef is very clever, he has no time to play games. Hence he asks you to help him. Write the program that solves this problem.

-----Input-----
The first line of the input contains an integer N denoting the number of elements in the given array. Next line contains N integers Ai separated with spaces. The third line contains the number of games T. Each of the next T lines contain 3 integers Li, Ri and Mi, the left side of the segment, the right side of segment and the modulo.

-----Output-----
For each game, output a single line containing the answer for the respective segment.

-----Constrdaints-----
- 1 ≤ N ≤ 100,000
- 1 ≤ Ai ≤ 100
- 1 ≤ T ≤ 100,000
- 1 ≤ Li ≤ Ri ≤ N
- 1 ≤ Mi ≤ 109

-----Example-----
Input:
5
1 2 3 4 5
4
1 2 3
2 3 4
1 1 1
1 5 1000000000

Output:
2
2
0
120
"""

import math

# Precomputed primes and their indices
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
dic = {prime: idx for idx, prime in enumerate(primes)}

def primeFactors(n, arr):
    """Helper function to update the prime factor counts in the array."""
    while n % 2 == 0:
        arr[dic[2]] += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            arr[dic[i]] += 1
            n = n // i
    if n > 2:
        arr[dic[n]] += 1
    return arr

def segment_multiplication(array, queries):
    """
    Calculate the segment multiplication for given queries.

    Parameters:
    - array: List of integers representing the array.
    - queries: List of tuples (Li, Ri, Mi) representing the queries.

    Returns:
    - List of integers representing the results of the queries.
    """
    N = len(array)
    tp = [0] * len(primes)
    dp = [tp]
    
    # Precompute the prime factor counts for each prefix of the array
    for i in range(1, N + 1):
        r = dp[i - 1].copy()
        t = primeFactors(array[i - 1], r)
        dp.append(t)
    
    results = []
    
    # Process each query
    for (l, r, m) in queries:
        if m == 1:
            results.append(0)
        else:
            ans = 1
            for i in range(len(primes)):
                ans = ans * pow(primes[i], dp[r][i] - dp[l - 1][i], m) % m
            results.append(ans % m)
    
    return results