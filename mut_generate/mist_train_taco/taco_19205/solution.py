"""
QUESTION:
Given a list A having N positive elements. The task to create another list such as i^{th} element is XOR of all elements of  A except A[i].
Example 1:
Input:
A = [2, 1, 5, 9]
Output:
13 14 10 6
Explanation:
At first position 1^5^9 = 13
At second position 2^5^9 = 14
At third position 2^1^9 = 10
At last position 2^1^5 = 6
Example 2:Ã¢â¬â¹
Input:
A = [2, 1]
Output:
1 2
Explanation: 
At first position except first position 
there is only one element = 1
At second position except second position
Ã¢â¬â¹there is only one element = 2
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getXor() which takes a list A and an integer N which is the size of the list A and return the modified list.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1), Where N is the size of the input array
Constraints:
1<= N <=10000
1<= A[i] <=100000
"""

def get_xors_except_self(A, N):
    """
    This function takes a list A and its size N as input, and returns a new list where each element at index i is the XOR of all elements in A except A[i].

    Parameters:
    A (list): A list of integers
    N (int): The size of the list A

    Returns:
    list: A list of integers where each element at index i is the XOR of all elements in A except A[i]
    """
    # Calculate the XOR of all elements in the list
    xor_all = 0
    for num in A:
        xor_all ^= num

    # For each element in the list, XOR it with the XOR of all elements
    # This effectively cancels out the current element, leaving the XOR of all other elements
    for i in range(N):
        A[i] = xor_all ^ A[i]

    return A