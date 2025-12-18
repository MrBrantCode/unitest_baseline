"""
QUESTION:
Given a number N, generate all the possible cyclic permutations of the number.
Example 1:
Input:
N = 123
Output:
123 312 231
Explanation:
For 123 there are 3 cyclic permutations possible.
Example 2:
Input:
N = 5674
Output:
5674 4567 7456 6745
Explanation:
For 5674 there are 4 cyclic permutations possible.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function cyclicPermutations() which takes an integer N as input parameter and returns the list of unique cyclic permutations of N.
Note: Cyclic permutation should not contain leading zeros
Expected Time Complexity: O(X)
Expected Auxiliary Space: O(X), Where X is the number of the digit of N.
Constraints: 
1 <= N <= 10^{9}
"""

def generate_cyclic_permutations(N: int) -> list[int]:
    l = [N]
    i = 1
    ln = len(str(N))
    mul = 10 ** (ln - 1)
    while i < ln:
        v = l[len(l) - 1]
        rem = v % 10
        qu = v // 10
        ans = mul * rem + qu
        if ans in l:
            break
        else:
            l.append(ans)
            i += 1
    return l