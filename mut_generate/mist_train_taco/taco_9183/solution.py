"""
QUESTION:
You are an owner of lemonade island, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by given array bills[]). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
NOTE: At first, you do not have any bill to provide changes with. You can provide changes from the bills that you get from the previous customers.
Given an integer array bills of size N where bills [ i ] is the bill the i^{th }customer pays, return true if you can provide every customer with the correct change, or false otherwise.
Example 1:
Input:
N = 5
bills [ ] = {5, 5, 5, 10, 20}
Output: True
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change we return true.
 
Example 2:
Input:
N = 5
bills [ ] = {5, 5, 10, 10, 20}
Output: False
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function lemonadeChange() which takes the interger N and integer array bills [ ] as parameters and returns true if it is possible to provide change to every customer otherwise false.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
bills[i] contains only {5, 10, 20}
"""

def can_provide_correct_change(bills: list[int]) -> bool:
    # Initialize the count of each bill type
    bill_count = {5: 0, 10: 0, 20: 0}
    
    # Iterate through each bill in the list
    for bill in bills:
        if bill == 5:
            # No change needed for a $5 bill
            bill_count[5] += 1
        elif bill == 10:
            # Need to give $5 change for a $10 bill
            if bill_count[5] > 0:
                bill_count[10] += 1
                bill_count[5] -= 1
            else:
                return False
        elif bill == 20:
            # Prefer to give $10 + $5 change for a $20 bill if possible
            if bill_count[10] > 0 and bill_count[5] > 0:
                bill_count[20] += 1
                bill_count[10] -= 1
                bill_count[5] -= 1
            # Otherwise, try to give $5 + $5 + $5 change
            elif bill_count[5] >= 3:
                bill_count[20] += 1
                bill_count[5] -= 3
            else:
                return False
    
    # If we made it through the loop, we can provide correct change to all customers
    return True