"""
QUESTION:
Your friend loves magic and he has coined a new term - "Magical number". To perform his magic, he needs that Magic number. There are N number of people in the magic show, seated according to their ages in ascending order. A magical number is that seat no. where the person has the same age as that of the given seat number.
Help your friend in finding out that "Magical number".
Note: If there are multiple magical numbers in the array, return the any one valid value.
Example:
Input:
1
10
-10 -1 0 3 10 11 30 50 100 150
Output:
3
Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N, size of an array.
The second line of each test case contains N input A[].
Output:
Print "Magical Number"
Print "-1" when the index value does not match with the value. 
Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 1000
-1000 ≤ A[i] ≤ 1000
"""

def find_magical_number(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    ans = -1
    while low <= high:
        m = (low + high) // 2
        if m == arr[m]:
            ans = arr[m]
            high = m - 1
        elif arr[m] > m:
            high = m - 1
        else:
            low = m + 1
    return ans