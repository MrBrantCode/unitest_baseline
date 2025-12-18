"""
QUESTION:
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:


       "123"
       "132"
       "213"
       "231"
       "312"
       "321"


Given n and k, return the kth permutation sequence.

Note:


       Given n will be between 1 and 9 inclusive.
       Given k will be between 1 and n! inclusive.


Example 1:


Input: n = 3, k = 3
Output: "213"


Example 2:


Input: n = 4, k = 9
Output: "2314"
"""

def get_kth_permutation(n: int, k: int) -> str:
    nums = list('123456789')[:n]  # Create a list of numbers from '1' to 'n'
    k -= 1  # Convert k to 0-based index
    factor = 1
    for i in range(1, n):
        factor *= i
    res = []
    for i in reversed(range(n)):
        res.append(nums[k // factor])
        nums.remove(nums[k // factor])
        if i:
            k %= factor
            factor //= i
    return ''.join(res)