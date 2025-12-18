"""
QUESTION:
Given an integer S. Find the largest even number that can be formed by rearranging the digits of S.
Note: In case the number does not contain any even digit then output the largest odd number possible.
Example 1:
Input:
S = "1324"
Output: "4312"
Explanation: Largest even number: 4312
Example 2:
Input:
S = "3555"
Output: "5553"
Explanation: No even number possible,
So we'll find largest odd number.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function LargestEven() which takes the string S as inputs representing the integer and returns the answer.
Expected Time Complexity: O(|S| * log |S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
S contains only digits from '0' to '9'.
"""

def largest_even_number(s: str) -> str:
    # Dictionary to count occurrences of each digit
    times = {str(i): 0 for i in range(10)}
    
    # Count the occurrences of each digit in the input string
    for digit in s:
        times[digit] += 1
    
    # Find the smallest even digit to place at the end
    smallest_even_digit = ''
    for even in range(0, 10, 2):
        t = str(even)
        if times[t] > 0:
            times[t] -= 1
            smallest_even_digit = t
            break
    
    # Construct the largest possible number by placing the remaining digits in descending order
    result = ''
    for i in range(9, -1, -1):
        t = str(i)
        if times[t] > 0:
            result += t * times[t]
    
    # Append the smallest even digit at the end
    result += smallest_even_digit
    
    return result