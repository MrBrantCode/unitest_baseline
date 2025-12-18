"""
QUESTION:
Given an Integer N and an array arr[] of length N. If index of the element is a Fibonacci Number, multiply the number by the index. After multiplying, if the number becomes greater than 100, make the element equal to the last two digits of the multiplied number. After doing these for all elements, find out the average of the N numbers in the Array.
Note: The array is in 1-based indexing (also in the Input). Also, print the floor value of the answer.
 
Example 1:
Input:
N = 5, arr[] = { 34, 78, 80, 91, 99 }
Output:
63
Explanation:
There are 5 elements.
1 is a fibonacci number and hence
34 is multiplied by 1.
2 is a fibonacci number and hence 78 is
multiplied by 2 and becomes 156 which being
greater than 100 is reduced to 56.
3 is a fibonacci number and hence 80 is
multiplied by 3 and it becomes 240, which
being greater than 100 is reduced to 40.
4 is not a fibonacci number and hence 91
is kept as it is.
5 is a fibonacci number and hence 99 is
multiplied by 5 and becomes 495 which being
greater than 100 is reduced to 95.
The total becomes 316 and the average is
63.2, floor of which is 63.
Example 2:
Input:
N = 2, arr[] = { 34, 99 }
Output:
66
Explanation:
There are 2 elements.
1 is a fibonacci number and hence
34 is multiplied by 1.
2 is a fibonacci number and hence 99 is
multiplied by 2 and becomes 198 which being
greater than 100 is reduced to 98.
The total becomes 132 and the average is 66.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getAvg() which takes an Integer N and an Array arr[] of length N as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 10^{5}
1 <= arr[i] <= 100
"""

def calculate_fibonacci_modified_average(N, arr):
    # Initialize the first two Fibonacci numbers
    fib = [0, 1]
    sum_modified = 0
    
    # Iterate through the array
    for j in range(N):
        # Check if the current index (1-based) is a Fibonacci number
        if j + 1 == fib[0] + fib[1]:
            # Multiply the element by its index
            v = arr[j] * (j + 1)
            # If the result is greater than 100, reduce it to the last two digits
            if v > 100:
                v %= 100
            # Update the array element
            arr[j] = v
            # Update the Fibonacci sequence
            (fib[0], fib[1]) = (fib[1], j + 1)
        
        # Accumulate the sum of the modified array elements
        sum_modified += arr[j]
    
    # Calculate the floor value of the average
    return sum_modified // N