"""
QUESTION:
We start with a permutation a_1, a_2, …, a_n and with an empty array b. We apply the following operation k times.

On the i-th iteration, we select an index t_i (1 ≤ t_i ≤ n-i+1), remove a_{t_i} from the array, and append one of the numbers a_{t_i-1} or a_{t_i+1} (if t_i-1 or t_i+1 are within the array bounds) to the right end of the array b. Then we move elements a_{t_i+1}, …, a_n to the left in order to fill in the empty space.

You are given the initial permutation a_1, a_2, …, a_n and the resulting array b_1, b_2, …, b_k. All elements of an array b are distinct. Calculate the number of possible sequences of indices t_1, t_2, …, t_k modulo 998 244 353.

Input

Each test contains multiple test cases. The first line contains an integer t (1 ≤ t ≤ 100 000), denoting the number of test cases, followed by a description of the test cases.

The first line of each test case contains two integers n, k (1 ≤ k < n ≤ 200 000): sizes of arrays a and b.

The second line of each test case contains n integers a_1, a_2, …, a_n (1 ≤ a_i ≤ n): elements of a. All elements of a are distinct.

The third line of each test case contains k integers b_1, b_2, …, b_k (1 ≤ b_i ≤ n): elements of b. All elements of b are distinct.

The sum of all n among all test cases is guaranteed to not exceed 200 000.

Output

For each test case print one integer: the number of possible sequences modulo 998 244 353.

Example

Input


3
5 3
1 2 3 4 5
3 2 5
4 3
4 3 2 1
4 3 1
7 4
1 4 7 3 6 2 5
3 2 4 5


Output


2
0
4

Note

\require{cancel}

Let's denote as a_1 a_2 … \cancel{a_i} \underline{a_{i+1}} … a_n → a_1 a_2 … a_{i-1} a_{i+1} … a_{n-1} an operation over an element with index i: removal of element a_i from array a and appending element a_{i+1} to array b.

In the first example test, the following two options can be used to produce the given array b:

  * 1 2 \underline{3} \cancel{4} 5 → 1 \underline{2} \cancel{3} 5 → 1 \cancel{2} \underline{5} → 1 2; (t_1, t_2, t_3) = (4, 3, 2); 
  * 1 2 \underline{3} \cancel{4} 5 → \cancel{1} \underline{2} 3 5 → 2 \cancel{3} \underline{5} → 1 5; (t_1, t_2, t_3) = (4, 1, 2). 



In the second example test, it is impossible to achieve the given array no matter the operations used. That's because, on the first application, we removed the element next to 4, namely number 3, which means that it couldn't be added to array b on the second step.

In the third example test, there are four options to achieve the given array b:

  * 1 4 \cancel{7} \underline{3} 6 2 5 → 1 4 3 \cancel{6} \underline{2} 5 → \cancel{1} \underline{4} 3 2 5 → 4 3 \cancel{2} \underline{5} → 4 3 5;
  * 1 4 \cancel{7} \underline{3} 6 2 5 → 1 4 3 \cancel{6} \underline{2} 5 → 1 \underline{4} \cancel{3} 2 5 → 1 4 \cancel{2} \underline{5} → 1 4 5;
  * 1 4 7 \underline{3} \cancel{6} 2 5 → 1 4 7 \cancel{3} \underline{2} 5 → \cancel{1} \underline{4} 7 2 5 → 4 7 \cancel{2} \underline{5} → 4 7 5;
  * 1 4 7 \underline{3} \cancel{6} 2 5 → 1 4 7 \cancel{3} \underline{2} 5 → 1 \underline{4} \cancel{7} 2 5 → 1 4 \cancel{2} \underline{5} → 1 4 5;
"""

def calculate_possible_sequences(n, k, a, b):
    MOD = 998244353
    
    # Create an index map for array `a`
    ind = [-1] * n
    for i in range(n):
        ind[a[i] - 1] = i
    
    # Mark the positions of elements in `b` in `a`
    fixed = [0] * n
    for i in range(k):
        fixed[ind[b[i] - 1]] = 1
    
    # Calculate the number of possible sequences
    ans = 1
    for i in range(k):
        curr = b[i] - 1
        temp = 0
        if ind[curr] > 0 and fixed[ind[curr] - 1] == 0:
            temp += 1
        if ind[curr] < n - 1 and fixed[ind[curr] + 1] == 0:
            temp += 1
        ans *= temp
        ans %= MOD
        fixed[ind[curr]] = 0
    
    return ans