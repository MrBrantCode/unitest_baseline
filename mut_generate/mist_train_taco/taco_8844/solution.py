"""
QUESTION:
There is a game that uses numbers called "Fizz Buzz". In this game, multiple players count the numbers one by one, starting with 1, and each player says only one number after the previous player. At that time, you must say "Fizz" if it is divisible by 3, "Buzz" if it is divisible by 5, and "FizzBuzz" if it is divisible by both. For example, the first 16 statements are as follows:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, ・ ・ ・

Taro decided to play "Fizz Buzz" with his friends. Taro and his colleagues decided the rules as follows.

"The wrong person will drop out. The next person will start with the next number after the wrong number. That is, if you say 1, 2, 3, you made a mistake with 3, so you will start with 4."

I play the game according to this rule, but because I am not used to the game, I sometimes do not notice that I made a mistake, and I cannot make a fair decision. So you decided to create a program that outputs the remaining people at the end of the set number of remarks so that Taro and his friends can enjoy this game.

Create a program that inputs the number of players, the number of times spoken during the game, and each statement, and outputs the number of the remaining players at the end of the input in ascending order. However, the players are numbered from 1, and the order of speaking is also from the first player, and when the speaking is completed, the first player will speak again. If the player in turn has already dropped out, the next player will speak. Also, the program must ignore subsequent statements when the player is alone.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


m n
s1
s2
::
sn


The first line gives the number of players m (2 ≤ m ≤ 1000) and the number of remarks n (1 ≤ n ≤ 10000).

The next n lines are given the i-th statement s1. si is an integer, Fizz, Buzz, or a string (up to 8 characters) that indicates FizzBuzz.

The number of datasets does not exceed 50.

Output

For each input dataset, the number of the player remaining when the specified number of remarks is input is output in ascending order.

Example

Input

5 7
1
2
Fizz
4
Buzz
6
7
3 5
1
2
3
4
5
0 0


Output

2 3 4 5
1
"""

def fizzbuzz_game(m, n, statements):
    def fizzbuzz(i):
        if i % 15 == 0:
            return 'FizzBuzz'
        elif i % 5 == 0:
            return 'Buzz'
        elif i % 3 == 0:
            return 'Fizz'
        else:
            return str(i)
    
    member = list(range(1, m + 1))
    pos = 0
    
    for i in range(n):
        if statements[i] != fizzbuzz(i + 1):
            del member[pos]
            m = len(member)
            if m == 1:
                break
        else:
            pos += 1
        pos %= m
    
    return member