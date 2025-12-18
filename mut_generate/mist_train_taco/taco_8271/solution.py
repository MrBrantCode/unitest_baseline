"""
QUESTION:
C: Divisor Game

problem

tsutaj is trying to play about a few games.

In a divisor game, a natural number N of 2 or more is given first, and then the game progresses according to the following procedure.

* Declare one integer from the divisors of N other than N. However, at this time, it is not possible to declare a divisor of an integer that has already been declared.
* Repeat this as long as there is an integer that can be declared, and if there is nothing that can be declared, the game ends.



Find the minimum and maximum number of possible declarations before the end of the game.

Input format

Input is given on one line.


N

Constraint

* 2 \ leq N \ leq 10 ^ {12}



Output format

Output the minimum and maximum number of declarations on one line separated by spaces.

Input example 1


18

Output example 1


twenty five

The following is an example of setting the number of declarations to 2.

* Declare 9.
* Declare 6. (6 is not a divisor of 9, so it can be declared)



If you do this, any integer that is a divisor of 18 and not 18 will be a divisor of the integers you have declared, and the game will end.

Note that you cannot declare anything that is a divisor of an integer that you have already declared. For example, you cannot declare 3 after declaring 9. Because 3 is a divisor of 9.

Input example 2


99

Output example 2


twenty five

Input example 3


10000000019

Output example 3


1 1

The input may not fit in a 32-bit integer type.





Example

Input

18


Output

2 5
"""

def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def divisor_game_declarations(N):
    yakusu = make_divisors(N)
    max_times = len(yakusu) - 1
    min_times = 0
    result = []
    for i in reversed(yakusu[:-1]):
        if i in result:
            continue
        result.extend(make_divisors(i))
        min_times += 1
    return min_times, max_times