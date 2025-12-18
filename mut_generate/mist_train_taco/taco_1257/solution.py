"""
QUESTION:
Count the given numbers on your fingers and find the correct finger on which the number ends.
	The first number starts from the thumb, second on the index finger, third on the middle finger, fourth on the ring finger and fifth on the little finger.
	Again six comes on the ring finger and so on.
	
Example 1:
Input:
N = 3
Output:
3
Explanation:
3 ends on the finger 3.
Example 2:
Input:
N = 6
Output:
4
Explanation:
6 ends on the finger 4.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function fingerCount() which takes an integer N as input parameter and returns the finger number on which this number ends.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^6
"""

def finger_count(N: int) -> int:
    rem = N % 8
    if not rem:
        return 2
    if rem <= 5:
        return rem
    else:
        return 5 - rem % 5