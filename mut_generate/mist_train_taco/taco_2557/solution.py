"""
QUESTION:
Given an array Arr[], write a program that segregates even and odd numbers. The program should put all even numbers first in sorted order, and then odd numbers in sorted order.
Note :- You don't have to return the array, you just have to modify it in-place.
Example 1:
Input: 
N = 7
Arr[] = {12, 34, 45, 9, 8, 90, 3}
Output: 8 12 34 90 3 9 45
Explanation: Even numbers are 12, 34,
8 and 90. Rest are odd numbers. After
sorting even numbers 8 12 34 90 and 
after sorting odd numbers 3 9 45. Then
concat both.
Example 2:
Input: 
N = 5
Arr[] = {0, 1, 2, 3, 4}
Output: 0 2 4 1 3
Explanation: 0 2 4 are even and 1 3
are odd numbers.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function segregateEvenOdd() which takes the array of integers arr[] and n as parameters and returns void. You need to modify the array itself.
Expected Time Complexity: O(N log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ Arr[i] <=10^{5}
"""

def segregate_even_odd(arr, n):
    # Separate even and odd numbers into two lists
    even_numbers = []
    odd_numbers = []
    
    for num in arr:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    
    # Sort both lists
    even_numbers.sort()
    odd_numbers.sort()
    
    # Concatenate sorted even and odd numbers
    sorted_arr = even_numbers + odd_numbers
    
    # Modify the original array in-place
    for i in range(n):
        arr[i] = sorted_arr[i]