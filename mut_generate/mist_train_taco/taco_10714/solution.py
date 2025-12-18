"""
QUESTION:
Given a non-negative number N. The task is to apply at most one swap operation on the number N so that the result is the smallest possible number.
Note: Input and Output should not contain leading zeros.
Example 1:
Input: N = "9625635"
Output: "2695635"
Explanation: Swapped the digits 9 and 2.
Example 2:
Input: N = "1205763"
Output: "1025763"
Explanation: Swapped the digits 0 and 2.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function smallestNumber() which takes the string as inputs and returns the answer.
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(|N|)
Constraints:
1 ≤ |N| ≤ 10^{5}
"""

def smallest_number_after_one_swap(num: str) -> str:
    num = list(num)
    str_num = num.copy()
    n = len(num)
    
    # Step 1: Create an array to store the index of the smallest digit to the right of each digit
    rightMin = [-1] * n
    right = n - 1
    rightMin[n - 1] = -1
    
    for i in range(n - 2, -1, -1):
        if num[i] >= num[right]:
            rightMin[i] = right
        else:
            rightMin[i] = -1
            right = i
    
    # Step 2: Handle the case where the first digit can be swapped with a non-zero digit
    small = -1
    mini = float('inf')
    
    for i in range(1, n):
        if str_num[i] == '0':
            for j in range(n - 1, -1, -1):
                if mini > int(str_num[j]) and str_num[j] != '0':
                    small = j
                    mini = int(str_num[j])
            (str_num[0], str_num[small]) = (str_num[small], str_num[0])
            break
    
    # Step 3: Swap the current digit with the smallest digit to its right if it makes the number smaller
    for i in range(n):
        if i != 0:
            if rightMin[i] != -1 and num[i] != num[rightMin[i]]:
                (num[i], num[rightMin[i]]) = (num[rightMin[i]], num[i])
                break
        elif rightMin[i] != -1 and num[rightMin[i]] != '0' and num[i] != num[rightMin[i]]:
            (num[i], num[rightMin[i]]) = (num[rightMin[i]], num[i])
            break
    
    # Step 4: Compare the two possible results and return the smaller one
    ans1 = ''.join(num)
    ans2 = ''.join(str_num)
    
    return ans1 if ans1 < ans2 else ans2