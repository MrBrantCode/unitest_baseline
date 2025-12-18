"""
QUESTION:
Today is the ticket release date for Aizu Entertainment's recommended idol group "Akabeko & Koboushi". There are four types of tickets:

S seat 6000 yen
A seat 4000 yen
B seat 3000 yen
C seat 2000 yen

You, the sales manager, are excitedly waiting for the launch. Finally on sale. It's selling very well!

Shortly after the launch, I received a table summarizing the orders up to that point. Each row of the table shows the type and number of tickets sold so far. However, the ticket types do not always appear in the order of S, A, B, C. Create a program to find the sales amount for each row in this table.



input

Input data is given in the following format.


t1 n1
t2 n2
t3 n3
t4 n4


The input consists of 4 lines. Line i is given the integer ti (1 ≤ ti ≤ 4) for the ticket type and the integer ni (0 ≤ ni ≤ 10000) for the number of tickets. The integers 1, 2, 3, and 4 representing the ticket types represent S seats, A seats, B seats, and C seats, respectively. Numbers from 1 to 4 always appear once as values ​​for t1, t2, t3, and t4, but they are not always given in the order of 1, 2, 3, 4.

output

Output the sales amount for each line.

Example

Input

3 10
1 4
4 1
2 5


Output

30000
24000
2000
20000
"""

def calculate_ticket_sales(ticket_orders):
    ticket_prices = {
        1: 6000,  # S seat
        2: 4000,  # A seat
        3: 3000,  # B seat
        4: 2000   # C seat
    }
    
    sales_amounts = []
    
    for t, n in ticket_orders:
        sales_amount = ticket_prices[t] * n
        sales_amounts.append(sales_amount)
    
    return sales_amounts