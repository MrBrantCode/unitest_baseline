"""
QUESTION:
Given an array with N elements, the task is to find the count of factors of a number X which is product of all array elements. 
 
Example 1:
Input:
N = 3
Arr[] = {2, 4, 6}
Output:
10
Explanation:
2 * 4 * 6 = 48, the factors of 48 are 
1, 2, 3, 4, 6, 8, 12, 16, 24, 48
whose count is 10.
 
Example 2:
Input:
N = 3
Arr[] = {3, 5, 7}
Output:
8
Explanation:
3 * 5 * 7 = 105, the factors of 105 are 
1, 3, 5, 7, 15, 21, 35, 105 whose count is 8.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countDivisorsMult() which takes the array A[] and its size N as inputs and returns the count of factors of X.
 
Expected Time Complexity: O(N. sqrt(N))
Expected Auxiliary Space: O(N)
 
Constraints:
2<=N<=10^{2}
1<=Arr[i]<=10^{2}
"""

from math import sqrt

def count_divisors_of_product(arr, n):
    prime_freq = {}
    
    # Factorize each number in the array
    for i in range(n):
        x = arr[i]
        j = 2
        while j * j <= x:
            while x % j == 0:
                prime_freq[j] = prime_freq.get(j, 0) + 1
                x //= j
            j += 1
        if x > 1:
            prime_freq[x] = prime_freq.get(x, 0) + 1
    
    # Calculate the count of divisors
    count = 1
    for freq in prime_freq.values():
        count *= freq + 1
    
    return count