"""
QUESTION:
An array is called beautiful if all the elements in the array are equal.

You can transform an array using the following steps any number of times: 

  1. Choose two indices i and j (1 ≤ i,j ≤ n), and an integer x (1 ≤ x ≤ a_i). Let i be the source index and j be the sink index. 
  2. Decrease the i-th element by x, and increase the j-th element by x. The resulting values at i-th and j-th index are a_i-x and a_j+x respectively. 
  3. The cost of this operation is x ⋅ |j-i| . 
  4. Now the i-th index can no longer be the sink and the j-th index can no longer be the source. 

The total cost of a transformation is the sum of all the costs in step 3.

For example, array [0, 2, 3, 3] can be transformed into a beautiful array [2, 2, 2, 2] with total cost 1 ⋅ |1-3| + 1 ⋅ |1-4| = 5.

An array is called balanced, if it can be transformed into a beautiful array, and the cost of such transformation is uniquely defined. In other words, the minimum cost of transformation into a beautiful array equals the maximum cost.

You are given an array a_1, a_2, …, a_n of length n, consisting of non-negative integers. Your task is to find the number of balanced arrays which are permutations of the given array. Two arrays are considered different, if elements at some position differ. Since the answer can be large, output it modulo 10^9 + 7.

Input

The first line contains a single integer n (1 ≤ n ≤ 10^5) — the size of the array. 

The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_i ≤ 10^9).

Output

Output a single integer — the number of balanced permutations modulo 10^9+7.

Examples

Input


3
1 2 3


Output


6

Input


4
0 4 0 4


Output


2

Input


5
0 11 12 13 14


Output


120

Note

In the first example, [1, 2, 3] is a valid permutation as we can consider the index with value 3 as the source and index with value 1 as the sink. Thus, after conversion we get a beautiful array [2, 2, 2], and the total cost would be 2. We can show that this is the only transformation of this array that leads to a beautiful array. Similarly, we can check for other permutations too.

In the second example, [0, 0, 4, 4] and [4, 4, 0, 0] are balanced permutations.

In the third example, all permutations are balanced.
"""

def count_balanced_permutations(n, a):
    M = 10**9 + 7
    
    # Calculate the sum of the array
    s = sum(a)
    
    # Check if the sum is divisible by n
    if s % n != 0:
        return 0
    
    # Calculate the target value for each element in the beautiful array
    s //= n
    
    # Initialize factorial array
    f = [1] * (n + 1)
    
    # Initialize buckets for counting elements greater, less, or equal to s
    b = [0] * 3
    
    # Dictionary to count occurrences of each element
    d = {}
    
    # Calculate factorials
    for i in range(2, n + 1):
        f[i] = f[i - 1] * i % M
    
    # Populate the dictionary and buckets
    for x in a:
        b[(x > s) - (x < s)] += 1
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    # Calculate the number of permutations
    k = 1
    for x in d.values():
        k *= f[x]
        k %= M
    
    k = f[n] * pow(k, M - 2, M) % M
    
    # Determine the result based on the counts in buckets
    if b[1] > 1 and b[-1] > 1:
        result = f[b[1]] * f[b[-1]] * 2 * pow(f[n - b[0]], M - 2, M) * k % M
    else:
        result = k % M
    
    return result