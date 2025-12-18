"""
QUESTION:
There is a ladder which leads to the door of heaven. Each step of ladder has a card in it. The card is blue if the number printed on it is even otherwise red.
Numbers on the ladder is in the following pattern :

1, 2, 3, 5, 8, 13, 21, 34, 55, 89

i.e., Number on the card of third step is equal to Sum of numbers printed on second and first step's card and similarly for the fourth step's card, number printed on it is equal to sum of numbers printed on card of steps third and second.

To unlock the door the Angel needs to know whether the person deserve heaven or not.

The person deserves heaven if and only if the person can tell her sum of all numbers printed on the blue cards.

Help the person to unlock the door to heaven.

Input Format

First line contains T  that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

i.e., Number on the card on last step of the ladder can be ≤ N and Number on card on 1st step of the ladder is 1

Output Format

Print the required answer for each test case.

Constraints

1 ≤ T ≤ 10^5

10 ≤ N ≤ 4×10^16

Sample Input

2
10
100

Sample Output

10
44

SAMPLE INPUT
2
10
100

SAMPLE OUTPUT
10
44
"""

def calculate_blue_card_sum(T, N_list):
    # Generate Fibonacci sequence up to the maximum N in N_list
    max_n = max(N_list)
    fibs = [1, 2]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max_n:
            break
        fibs.append(next_fib)
    
    # Calculate the sum of even Fibonacci numbers for each N
    results = []
    for n in N_list:
        sum_even_fibs = sum(num for num in fibs if num <= n and num % 2 == 0)
        results.append(sum_even_fibs)
    
    return results