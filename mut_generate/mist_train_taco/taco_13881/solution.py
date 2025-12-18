"""
QUESTION:
Chef has an array A of length N.

He calls an index i (1 ≤ i ≤ N) *good* if there exists some j \neq i such that A_{i} = A_{j}.

Chef can perform the following operation at most once:

Choose any [subsequence] of the array A and add any positive integer to all the elements of the chosen subsequence.

Determine the maximum number of good indices Chef can get.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains a single integer N denoting the length of the array A.
- The second line contains N space-separated integers denoting the array A.

------ Output Format ------ 

For each test case, output the maximum number of good indices Chef can get after performing the given operation at most once.

------ Constraints ------ 

$1 ≤ T ≤ 500$
$2 ≤ N ≤ 1000$
$1 ≤ A_{i} ≤ 1000$
- The sum of $N$ over all test cases won't exceed $2000$.

----- Sample Input 1 ------ 
3
6
1 3 5 2 4 8
4
2 3 4 5
7
1 1 2 2 3 4 4

----- Sample Output 1 ------ 
4
4
7
"""

def max_good_indices(A: list) -> int:
    """
    Determines the maximum number of good indices Chef can get after performing the given operation at most once.

    Parameters:
    A (list): The array of integers.

    Returns:
    int: The maximum number of good indices.
    """
    freq = {}
    for i in A:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    A = [*freq.keys()]
    A.sort()
    max_count = sum((freq[x] for x in freq if freq[x] > 1))
    for x in range(1, A[-1] - A[0] + 1):
        (s, p, count) = ([], {}, 0)
        for i in A:
            if i - x in freq:
                p[i] = p[i - x]
            else:
                p[i] = len(s)
                s.append([])
            s[p[i]].append(freq[i])
        for v in s:
            count += sum(v)
            v.sort()
            if len(v) & 1 and v[-1] == 1:
                count -= 1
        max_count = max(max_count, count)
    return max_count