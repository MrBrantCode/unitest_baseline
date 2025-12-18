"""
QUESTION:
Given an array Arr[] of N integers.Find the sum of values of even and odd index positions separately.
Example 1:
Input:
N=5
Arr={1,2,3,4,5}
Output:
9 6
Explanation:
The sum of elements at odd places i.e
at 1st,3rd and 5th places are (1+3+5=9)
Similarly,the sum of elements at even 
places i.e. at 2nd and 4th places are
(2+4=6).
Example 2:
Input:
N=5
Arr={1,1,1,1,1}
Output:
3 2
Explanation:
The sum of elements at odd places
is (1+1+1=3).Similarly, the sum of
elements at even places is (1+1=2)
Your Task:
You don't need to read input or print anything.Your Task is to complete the function EvenOddSum() which takes an integer N and an array Arr as input parameters and returns the sum of elements in odd places and in even places separately.
 
Expected Time Complexity:O(N)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{5}
0<=Arr[i]<=10^{4},for 0<=i
"""

def calculate_even_odd_sums(N, Arr):
    sum_even = 0
    sum_odd = 0
    for i in range(N):
        if i % 2 == 0:
            sum_even += Arr[i]
        else:
            sum_odd += Arr[i]
    return (sum_even, sum_odd)