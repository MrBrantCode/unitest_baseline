"""
QUESTION:
You are given an array A of size N. You are also given an integer Q. Can you figure out the answer to each of the Q queries?

Each query contains 2 integers x and y, and you need to find whether the value find(x,y) is Odd or Even:

find(int x,int y)
{
    if(x>y) return 1;
    ans = pow(A[x],find(x+1,y))
    return ans
}

Note : pow(a,b) = a^{b}.

Input Format 

The first line of the input contains an integer N. 
The next line contains N space separated non-negative integers(whole numbers less than or equal to 9). 

The line after that contains a positive integer, Q , the denotes the number of queries to follow.
Q lines follow, each line contains two positive integer x and y separated by a single space.   

Output Format 

For each query, display 'Even' if the value returned is Even, otherwise display 'Odd'.

Constraints 

2 ≤ N ≤ 10^{5} 

2 ≤ Q ≤ 10^{5} 

1 ≤ x,y ≤ N 

x ≤ y

Array is 1-indexed.  

No 2 consecutive entries in the array will be zero.

Sample Input 

3
3 2 7
2
1 2
2 3

Sample Output 

Odd
Even

Explanation

find(1,2) = 9, which is Odd 

find(2,3) = 128, which is even
"""

def find_parity(A, x, y):
    # Convert 1-indexed to 0-indexed
    x -= 1
    y -= 1
    
    # Base case: if x > y, return 1 (which is odd)
    if x > y:
        return 'Odd'
    
    # Check if the first element is odd
    if A[x] % 2 == 1:
        return 'Odd'
    
    # If the first element is even, check the next element
    if x < y and A[x + 1] == 0:
        return 'Odd'
    
    return 'Even'