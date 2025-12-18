"""
QUESTION:
Like people, numbers are also friends with each other. Friendliness between any two numbers a and b is defined as the absolute difference between the two. Lower is this number more friendly the numbers are. Now you are given an array of numbers and you are required to find the friendliness of this array. This can be calculated as the sum of the friendliness of each element in the array with its closest friend in the same array. 
Example 1:
Input:
N=3
arr[] = { 4,1,5 }
Output: 5
Explanation: Sum of absolute differences is
            |4-5| + |1-4| + |5-4| = 5
Example 2:
Input:
N=3
arr[] = { 1,1,1 }
Output: 0
Explanation: Sum of absolute differences is 
             |1-1| + |1-1| + |1-1| = 0
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function sumOfMinAbsDifferences() that takes array arr and integer N as parameters and return the value of friendliness for the given array.
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(1).
Constraints:
2 ≤ N ≤ 10^{5}
"""

def calculate_friendliness(arr, N):
    arr.sort()
    s = 0
    for index in range(1, N - 1):
        one = abs(arr[index] - arr[index + 1])
        two = abs(arr[index] - arr[index - 1])
        s += min(one, two)
    s += abs(arr[-1] - arr[-2])
    s += abs(arr[1] - arr[0])
    return s