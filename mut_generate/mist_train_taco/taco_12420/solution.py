"""
QUESTION:
Given a number n, find the smallest number that has the same set of digits as n and is greater than n. If n is the greatest possible number with its set of digits, report it.
Example 1:
Input:
N = 143
Output: 314
Explanation: Numbers possible with digits
1, 3 and 4 are: 134, 143, 314, 341, 413, 431.
The first greater number after 143 is 314.
Example 2:
Input:
N = 431
Output: not possible
Explanation: Numbers possible with digits
1, 3 and 4 are: 134, 143, 314, 341, 413, 431.
Clearly, there's no number greater than 431.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findNext () which takes an integer N as input and returns the smallest number greater than N with the same set of digits as N. If such a number is not possible, return -1.
Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(LogN).
Constraints:
1 ≤ N ≤ 100000
"""

def find_next_greater_number(n: int) -> int:
    # Convert the number to a list of digits
    s = []
    temp = n
    while temp > 0:
        k = temp % 10
        s.append(k)
        temp //= 10
    s = s[::-1]
    N = len(s)
    arr = s
    
    # Find the first digit that is smaller than the digit next to it
    idx = N - 1
    for i in range(N - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            idx = i
            break
    
    # If no such digit is found, return -1
    if idx == N - 1:
        return -1
    
    # Find the smallest digit on right side of (idx) which is greater than arr[idx]
    for i in range(idx + 1, N):
        if arr[idx] >= arr[i]:
            (arr[i - 1], arr[idx]) = (arr[idx], arr[i - 1])
            break
        elif i == N - 1:
            (arr[i], arr[idx]) = (arr[idx], arr[i])
    
    # Reverse the digits after (idx)
    arr = arr[:idx + 1] + arr[N - 1:idx:-1]
    
    # Convert the list of digits back to a number
    res = ''
    i = 0
    while i < len(arr):
        res += str(arr[i])
        i += 1
    
    return int(res)