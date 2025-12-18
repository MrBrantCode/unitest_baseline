"""
QUESTION:
Each of you probably has your personal experience of riding public transportation and buying tickets. After a person buys a ticket (which traditionally has an even number of digits), he usually checks whether the ticket is lucky. Let us remind you that a ticket is lucky if the sum of digits in its first half matches the sum of digits in its second half.

But of course, not every ticket can be lucky. Far from it! Moreover, sometimes one look at a ticket can be enough to say right away that the ticket is not lucky. So, let's consider the following unluckiness criterion that can definitely determine an unlucky ticket. We'll say that a ticket is definitely unlucky if each digit from the first half corresponds to some digit from the second half so that each digit from the first half is strictly less than the corresponding digit from the second one or each digit from the first half is strictly more than the corresponding digit from the second one. Each digit should be used exactly once in the comparisons. In other words, there is such bijective correspondence between the digits of the first and the second half of the ticket, that either each digit of the first half turns out strictly less than the corresponding digit of the second half or each digit of the first half turns out strictly more than the corresponding digit from the second half.

For example, ticket 2421 meets the following unluckiness criterion and will not be considered lucky (the sought correspondence is 2 > 1 and 4 > 2), ticket 0135 also meets the criterion (the sought correspondence is 0 < 3 and 1 < 5), and ticket 3754 does not meet the criterion. 

You have a ticket in your hands, it contains 2n digits. Your task is to check whether it meets the unluckiness criterion.

Input

The first line contains an integer n (1 ≤ n ≤ 100). The second line contains a string that consists of 2n digits and defines your ticket.

Output

In the first line print "YES" if the ticket meets the unluckiness criterion. Otherwise, print "NO" (without the quotes).

Examples

Input

2
2421


Output

YES


Input

2
0135


Output

YES


Input

2
3754


Output

NO
"""

def is_definitely_unlucky_ticket(n, ticket_number):
    # Convert the ticket number into a list of characters (digits)
    ticket_number = list(ticket_number)
    
    # Split the ticket number into two halves
    first_half = ticket_number[:n]
    second_half = ticket_number[n:]
    
    # Sort both halves
    first_half.sort()
    second_half.sort()
    
    # Initialize a flag to determine if the ticket is definitely unlucky
    flag = 1
    
    # Check if all digits in the first half are strictly less than or greater than the corresponding digits in the second half
    if first_half[0] > second_half[0]:
        for i in range(n):
            if first_half[i] <= second_half[i]:
                flag = 0
                break
    else:
        for i in range(n):
            if first_half[i] >= second_half[i]:
                flag = 0
                break
    
    # Return "YES" if the ticket is definitely unlucky, otherwise "NO"
    return 'YES' if flag == 1 else 'NO'