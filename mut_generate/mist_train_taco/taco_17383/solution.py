"""
QUESTION:
Given a number S in the form of string, the task is to check whether the sum of digits at odd places is equal to the sum of digits at even places or not.
Example 1:
Input: S = "132"
Output: 1
Explanation: The sum of digits at odd 
places is 1+2=3. Similarly the sum of 
digits at even places is 3. Since they 
are equal,the answer is 1.
Example 2:
Input: S = "123"
Output: 0
Explanation: The sum of digits at odd 
places is 1+3=4. The sum of digits at 
even places is 2. Since,the sums are 
not equal,Thus answer is 0.
Your Task:
You don't need to read input or print anything.Your task is to complete the function oddAndEven() which takes an integer S (in the form of string) as input parameter and returns 1 if the sum of digits at odd places is equal to the sum of digits at even places.Otherwise, it returns 0.
Expected Time Complexity:O(|S|)
Expected Auxillary Space:O(1)
Constraints:
1≤ |S| ≤ 10^{5}
"""

def check_sum_parity(S: str) -> int:
    odd_sum = 0
    even_sum = 0
    
    for i in range(len(S)):
        if i % 2 == 0:
            odd_sum += int(S[i])
        else:
            even_sum += int(S[i])
    
    return 1 if odd_sum == even_sum else 0