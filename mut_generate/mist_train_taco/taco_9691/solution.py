"""
QUESTION:
Given a non-negative number num in the form of string. The task is to apply at most one swap operation on the number num so that the result is the next higher number.
Example 1:
Input: num = "768"
Output: "786"
Explanation: This is next higher
number that we can get.
Example 2:
Input: num = "333"
Output: "-1"
Explanation: There is no higher
number than 333. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function nxtHighUsingAtMostOneSwap() which takes the string num as inputs and returns the answer.
Expected Time Complexity: O(|num|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |num| ≤ 10^{5}
|num| denotes the length of the string num.
"""

def next_higher_number_with_one_swap(num: str) -> str:
    a = [c for c in num]
    n = len(num)
    marked = [-1] * 10
    marked[ord(a[n - 1]) - ord('0')] = n - 1
    
    for i in range(n - 2, -1, -1):
        pos = -1
        for j in range(ord(a[i]) - ord('0') + 1, 10):
            if marked[j] != -1 and (pos == -1 or pos < marked[j]):
                pos = marked[j]
        if pos != -1:
            (a[pos], a[i]) = (a[i], a[pos])
            num2 = ''.join(a)
            return num2
        marked[ord(a[i]) - ord('0')] = i
    
    return '-1'