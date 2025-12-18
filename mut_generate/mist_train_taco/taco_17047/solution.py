"""
QUESTION:
Geek has N dollars in his bank account. He wants to withdraw all of it but the bank only allows withdrawal of an amount that is a divisor of the current amount in the bank and is less than the current amount.
If Geek withdraws the maximum possible amount each day, how many days does he need to take out all of his money from the bank? 
Note: If the remaining amount is 1, he can withdraw it.
 
Example 1:
Input: N = 12
Output: 5
Explanation: N = 12
Withdraws 6, Remaining = 6
Withdraws 3, Remaining = 3
Withdraws 1, Remaining = 2
Withdraws 1, Remaining = 1
Withdraws 1, Remaining = 0
 
Example 2:
Input: N = 21
Output: 7
Explanation: N = 21
Withdraws 7, Remaining = 14
Withdraws 7, Remaining = 7
Withdraws 1, Remaining = 6
Withdraws 3, Remaining = 3
Withdraws 1, Remaining = 2
Withdraws 1, Remaining = 1
Withdraws 1, Remaining = 0
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfDays() which takes an integer N as input parameter and returns the number of days Geek needs to withdraw all of his money. 
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints : 
1 <= N <= 10^{12}
"""

def calculate_withdrawal_days(N):
    days = 0
    while N > 0:
        check = 0
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                N -= N // i
                days += 1
                check = 1
                break
        if check == 0:
            N -= 1
            days += 1
    return days