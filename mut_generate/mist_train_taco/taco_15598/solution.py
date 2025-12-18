"""
QUESTION:
There are N cards on the table and each has a number between 0 and N. Let us denote the number on the i^{th} card by c_{i}. You want to pick up all the cards. The i^{th} card can be picked up only if at least c_{i} cards have been picked up before it. (As an example, if a card has a value of 3 on it, you can't pick that card up unless you've already picked up 3 cards previously) In how many ways can all the cards be picked up?

Input Format 

The first line contains the number of test cases T. T test cases follow. Each case contains an integer N on the first line, followed by integers c_{1},..c_{i},...,c_{N} on the second line.

Output Format 

Output T lines one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo 1000000007.

Constraints: 

1 <= T <= 10 

1 <= N <= 50000 

0 <= c_{i} <= N

Sample Input:  

3  
3  
0 0 0  
3  
0 0 1  
3  
0 3 3

Sample Output:  

6  
4  
0

Sample Explanations:

For the first case, the cards can be picked in any order, so there are 3! = 6 ways. 

For the second case, the cards can be picked in 4 ways: {1,2,3}, {2,1,3}, {1,3,2}, {2,3,1}.  

For the third case, no cards can be picked up after the first one, so there are 0 ways to pick up all cards.
"""

def calculate_card_pickup_ways(test_cases):
    MOD = 10**9 + 7
    results = []
    
    for case in test_cases:
        N, cards = case
        cards.sort()
        ways = 1
        
        for i in range(N):
            if i < cards[i]:
                ways = 0
                break
            else:
                ways *= (i + 1 - cards[i])
                ways %= MOD
        
        results.append(ways)
    
    return results