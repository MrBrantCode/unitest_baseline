"""
QUESTION:
Cows in the FooLand city are interesting animals. One of their specialities is related to producing offsprings. A cow in FooLand produces its first calve (female calf) at the age of two years and proceeds to produce other calves (one female calf a year).
Now the farmer Harold wants to know how many animals would he have at the end of N years, if we assume that none of the calves dies, given that initially, he has only one female calf?
Since the answer can be huge, print it modulo 10^{9}+7.
 
Example 1:
Input: N = 2
Output: 2
Explanation: At the end of 1 year, he will have 
only 1 cow, at the end of 2 years he will have 
2 animals (one parent cow C1 and other baby 
calf B1 which is the offspring of cow C1).
Example 2:
Input: N = 4
Output: 5
Explanation: At the end of 1 year, he will have
only 1 cow, at the end of 2 years he will have
2 animals (one parent cow C1 and other baby
calf B1 which is the offspring of cow C1). At
the end of 3 years, he will have 3 animals (one
parent cow C1 and 2 female calves B1 and B2, C1
is the parent of B1 and B2).At the end of 4 
years,he will have 5 animals (one parent cow C1,
3 offsprings of C1 i.e. B1, B2, B3 and one 
offspring of B1).
 
Your Task:
You don't need to read or print anything. Your task is to complete the function TotalAnimal() which takes N as input parameter and returns the total number of animals at the end of N years modulo 10^{9} + 7.
 
Expected Time Complexity: O(log_{2}N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def calculate_total_animals(N: int) -> int:
    def multiple(a, b, m):
        ans = [[0, 0], [0, 0]]
        ans[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
        ans[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
        ans[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
        ans[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
        return ans

    def binpow(a, n, m):
        ans = [[1, 0], [0, 1]]
        while n > 0:
            if n & 1:
                ans = multiple(ans, a, m)
            a = multiple(a, a, m)
            n >>= 1
        return ans

    M = 1000000007
    a = [[1, 1], [1, 0]]
    a = binpow(a, N, M)
    return a[0][0]