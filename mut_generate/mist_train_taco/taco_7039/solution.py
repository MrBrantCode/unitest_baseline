"""
QUESTION:
There are 'n' coins kept on the table, numbered from 0 to 'n-1'. Initially, each coin is kept tails up. You have to perform two types of operations :
1) Flip all coins numbered between A and B inclusive. This is represented by the command:
0
A
B
2) Answer how many coins numbered between A and B inclusive are heads up. This is represented by the command
1
A
B

Input:
The first two lines contain two integers, N and Q.The first line after inputting  N and Q has to be  of form (1).Each of the next Q lines are of the form (2) as mentioned above.
Output:
Output 1 line for each of the queries of the form 2 containing the required answer for the corresponding query just after the query.
7 
3
0 
3
5
1 
0 
6
3     <-- this is the first output
1
3
4 
2    <-- this is output

SAMPLE INPUT
7
3
0
3
5
1
0
6
1
3
4

SAMPLE OUTPUT
3
2
"""

def process_coin_operations(n, operations):
    coins = ['T'] * n  # Initialize all coins as tails
    results = []
    
    for op in operations:
        command, A, B = op
        if command == 0:
            # Flip coins from A to B inclusive
            for i in range(A, B + 1):
                coins[i] = 'H' if coins[i] == 'T' else 'T'
        elif command == 1:
            # Count heads from A to B inclusive
            results.append(coins[A:B + 1].count('H'))
    
    return results