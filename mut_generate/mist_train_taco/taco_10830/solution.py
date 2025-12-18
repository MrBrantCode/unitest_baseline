"""
QUESTION:
Given a number N, find the most occurring digit in it. If two or more digits occur same number of times, then return the highest of them. Input number is given as a string.
Example 1:
Input:
N = "12234"
Output:
2
Explanation :
2 occurs most times
Example 2:
Input:
N = "1122"
Output:
2
Explanation :
1 and 2 occurs most times but 2 > 1.
 
Your Task: 
You don't need to read input or print anything. Your task is to complete the function solve() that receives a string N as input parameter and returns the most frequent digit in it as a string.
Expected Time Complexity : O(len(N))
Expected Space Complexity : O(1)
Constraints:
1<= len(N) <=101000
"""

def most_frequent_digit(N: str) -> str:
    digit_count = {}
    max_count = 1
    
    # Count the frequency of each digit
    for digit in N:
        if digit in digit_count:
            digit_count[digit] += 1
            if digit_count[digit] > max_count:
                max_count = digit_count[digit]
        else:
            digit_count[digit] = 1
    
    # Collect all digits that have the maximum frequency
    most_frequent_digits = []
    for digit in N:
        if digit_count[digit] == max_count:
            most_frequent_digits.append(int(digit))
    
    # Return the highest digit among the most frequent ones
    return str(max(most_frequent_digits))