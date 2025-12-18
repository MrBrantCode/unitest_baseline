"""
QUESTION:
Alice and Bob are playing a game on a sequence $a_1, a_2, \dots, a_n$ of length $n$. They move in turns and Alice moves first.

In the turn of each player, he or she should select an integer and remove it from the sequence. The game ends when there is no integer left in the sequence.

Alice wins if the sum of her selected integers is even; otherwise, Bob wins.

Your task is to determine who will win the game, if both players play optimally.


-----Input-----

Each test contains multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 100$) — the number of test cases. The following lines contain the description of each test case.

The first line of each test case contains an integer $n$ ($1 \leq n \leq 100$), indicating the length of the sequence.

The second line of each test case contains $n$ integers $a_1, a_2, \dots, a_n$ ($-10^9 \leq a_i \leq 10^9$), indicating the elements of the sequence.


-----Output-----

For each test case, output "Alice" (without quotes) if Alice wins and "Bob" (without quotes) otherwise.


-----Examples-----

Input
4
3
1 3 5
4
1 3 5 7
4
1 2 3 4
4
10 20 30 40
Output
Alice
Alice
Bob
Alice


-----Note-----

In the first and second test cases, Alice always selects two odd numbers, so the sum of her selected numbers is always even. Therefore, Alice always wins.

In the third test case, Bob has a winning strategy that he always selects a number with the same parity as Alice selects in her last turn. Therefore, Bob always wins.

In the fourth test case, Alice always selects two even numbers, so the sum of her selected numbers is always even. Therefore, Alice always wins.
"""

def determine_winner(test_cases):
    results = []
    for n, a in test_cases:
        odd = 0
        even = 0
        for x in a:
            if x % 2 == 0:
                even += 1
            else:
                odd += 1
        if even % 2 == 1 and odd % 4 != 2:
            results.append('Alice')
        elif even % 2 == 1:
            results.append('Bob')
        elif 1 <= odd % 4 <= 2:
            results.append('Bob')
        else:
            results.append('Alice')
    return results