"""
QUESTION:
A cafe has N computers. Several customers come to the cafe to use these computers. A customer will be serviced only if there is any unoccupied computer at the moment the customer visits the cafe. If there is no unoccupied computer, the customer leaves the cafe. 
You are given an integer N representing the number of computers in the cafe and a sequence of uppercase letters S. Every letter in S occurs exactly two times. The first occurrence denotes the arrival of a customer and the second occurrence denotes the departure of the same customer if he gets allocated the computer. 
You have to find the number of customers that walked away without using a computer.
Example 1:
Input:
N = 3
S = GACCBDDBAGEE
Output: 1
Explanation: Only D will not be able to 
get any computer. So the answer is 1.
Example 2:
N = 1
S = ABCBAC
Output: 2
Explanation: B and C will not be able to 
get any computers. So the answer is 2.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes the integer N (the number of computers in the cafe) and the string S (denoting the arrival and departure of a customer) as input parameters and returns an integer representing the number of customers that walked away without using a computer.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 26
1 <= |S| <= 52
S consists of uppercase English letters and each letter occurs exactly 2 times.
"""

def count_customers_without_computer(N, S):
    ans = 0
    l = [0] * 26
    k = N
    res = 0
    for i in S:
        p = ord(i) - 65
        if l[p] == 1:
            k += 1
            l[p] = 0
        elif l[p] == 0:
            if k == 0:
                ans += 1
                l[p] = -1
            else:
                k -= 1
                l[p] = 1
    return ans