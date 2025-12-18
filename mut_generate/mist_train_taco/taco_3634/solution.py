"""
QUESTION:
Taro and Hanako have numbers of cards in their hands. Each of the cards has a score on it. Taro and Hanako wish to make the total scores of their cards equal by exchanging one card in one's hand with one card in the other's hand. Which of the cards should be exchanged with which?

Note that they have to exchange their cards even if they already have cards of the same total score.

Input

The input consists of a number of datasets. Each dataset is formatted as follows.

> n m
>  s1
>  s2
>  ...
>  sn
>  sn+1
>  sn+2
>  ...
>  sn+m
>

The first line of a dataset contains two numbers n and m delimited by a space, where n is the number of cards that Taro has and m is the number of cards that Hanako has. The subsequent n+m lines list the score for each of the cards, one score per line. The first n scores (from s1 up to sn) are the scores of Taro's cards and the remaining m scores (from sn+1 up to sn+m) are Hanako's.

The numbers n and m are positive integers no greater than 100. Each score is a non-negative integer no greater than 100.

The end of the input is indicated by a line containing two zeros delimited by a single space.

Output

For each dataset, output a single line containing two numbers delimited by a single space, where the first number is the score of the card Taro gives to Hanako and the second number is the score of the card Hanako gives to Taro. If there is more than one way to exchange a pair of cards that makes the total scores equal, output a pair of scores whose sum is the smallest.

In case no exchange can make the total scores equal, output a single line containing solely -1. The output must not contain any superfluous characters that do not conform to the format.

Sample Input


2 2
1
5
3
7
6 5
3
9
5
2
3
3
12
2
7
3
5
4 5
10
0
3
8
1
9
6
0
6
7 4
1
1
2
1
2
1
4
2
3
4
3
2 3
1
1
2
2
2
0 0


Output for the Sample Input


1 3
3 5
-1
2 2
-1






Example

Input

2 2
1
5
3
7
6 5
3
9
5
2
3
3
12
2
7
3
5
4 5
10
0
3
8
1
9
6
0
6
7 4
1
1
2
1
2
1
4
2
3
4
3
2 3
1
1
2
2
2
0 0


Output

1 3
3 5
-1
2 2
-1
"""

def find_card_exchange(n, m, taro_cards, hanako_cards):
    ans = []
    
    for i in range(n):
        for j in range(m):
            if sum(taro_cards) - taro_cards[i] + hanako_cards[j] == sum(hanako_cards) - hanako_cards[j] + taro_cards[i]:
                ans.append([taro_cards[i] + hanako_cards[j], taro_cards[i], hanako_cards[j]])
    
    ans = sorted(ans)
    
    if len(ans) != 0:
        return (ans[0][1], ans[0][2])
    else:
        return -1