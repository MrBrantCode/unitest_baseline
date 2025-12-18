"""
QUESTION:
Given an array arr of size N, the task is to count the number of elements of the array which are Fibonacci numbers
Example 1:
Input: N = 9, arr[] = {4, 2, 8, 5, 20, 1, 
                              40, 13, 23}
Output: 5
Explanation: Here, Fibonacci series will 
be 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. 
Numbers that are present in array are 
2, 8, 5, 1, 13
Example 2:
Input: N = 4, arr[] = {4, 7, 6, 25} 
Output: 0
Explanation: No Fibonacci number in 
this array.
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function checkFib() that takes array arr and integer N as parameters and returns the desired output.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}
"""

def count_fibonacci_numbers(arr, N):
    # Find the maximum number in the array to limit the Fibonacci sequence generation
    max_num = max(arr)
    
    # Initialize the list to store Fibonacci numbers
    fib_numbers = [0, 1]
    
    # Generate Fibonacci numbers until the maximum number in the array
    i = 2
    while True:
        next_fib = fib_numbers[i - 1] + fib_numbers[i - 2]
        if next_fib > max_num:
            break
        fib_numbers.append(next_fib)
        i += 1
    
    # Count the Fibonacci numbers in the array
    fib_count = 0
    for num in arr:
        if num in fib_numbers:
            fib_count += 1
    
    return fib_count