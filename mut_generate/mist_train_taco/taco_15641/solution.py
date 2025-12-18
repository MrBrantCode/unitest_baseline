"""
QUESTION:
You are given an array A of size N, and you are also given a sum. You need to find if two numbers in A exist that have sum equal to the given sum.
Examples:
Input:
1
10
1 2 3 4 5 6 7 8 9 10
14
Output:
1
Input Format:
The first line of input contains T denoting the number of test cases. T test cases follow. Each test case contains three lines of input. The first line contains N denoting the size of the array A. The second line contains N elements of the array. The third line contains the element sum.
Output Format:
For each test case, in a new line, print the required output.
Your Task:
Since this is a function problem, you don't need to take any input. Just complete the provided function sumExists().
Constraints:
1 <= T <= 100
1 <= N <= 1000
1 <= A_{i} <= 10^{6}
"""

def sum_exists(arr, n, Sum):
    arr.sort()
    i, j = 0, n - 1
    while i < j:
        if arr[i] + arr[j] == Sum:
            return 1
        elif arr[i] + arr[j] > Sum:
            j -= 1
        else:
            i += 1
    return 0