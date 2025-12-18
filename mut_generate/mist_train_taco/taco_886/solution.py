"""
QUESTION:
Given a string S consisting of only lowercase characters. Find the lexicographically smallest string after removing exactly k characters from the string. But you have to correct the value of k, i.e., if the length of the string is a power of 2, reduce k by half, else multiply k by 2. You can remove any k character.
NOTE: If it is not possible to remove k (the value of k after correction) characters or if the resulting string is empty return -1. 
Example 1:
Input: S = "fooland", k = 2
Output: "and" 
Explanation: As the size of the string = 7
which is not a power of 2, hence k = 4.
After removing 4 characters from the given 
string, the lexicographically smallest
string is "and".
Example 2:
Input: S = "code", k = 4
Output: "cd"
Explanation: As the length of the string = 4, 
which is 2 to the power 2, hence k = 2.
Hence, lexicographically smallest string after 
removal of 2 characters is "cd".
Your Task:  
You dont need to read input or print anything. Complete the function lexicographicallySmallest() which takes S and k as input parameters and returns the lexicographically smallest string after removing k characters.
Expected Time Complexity: O(n+k), n is size of the string
Expected Auxiliary Space: O(n)
Constraints:
1<= |S| <=10^{5}
1<= k <= 10^{5}
"""

from collections import deque

def is_power_of_two(n):
    return (n & (n - 1)) == 0

def lexicographically_smallest_string(S, k):
    st = deque()
    top = -1
    n = len(S)
    
    # Correct the value of k based on the length of the string
    if is_power_of_two(n):
        k = k // 2
    else:
        k = 2 * k
    
    # If k is greater than or equal to the length of the string, return '-1'
    if k >= n:
        return '-1'
    
    # Process the string to find the lexicographically smallest string
    for ch in S:
        while k > 0 and top >= 0 and (ch < st[top]):
            st.pop()
            k -= 1
            top -= 1
        st.append(ch)
        top += 1
    
    # Remove additional characters if k is still greater than 0
    while k > 0 and top != -1:
        st.pop()
        top -= 1
        k -= 1
    
    # Construct the resulting string
    ans = ''
    while top >= 0:
        ans = st.pop() + ans
        top -= 1
    
    return ans