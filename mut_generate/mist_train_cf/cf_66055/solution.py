"""
QUESTION:
Create a function named `divisorGame` that takes an integer `n` as input, where `2 <= n <= 1000`, and returns a boolean value indicating whether Alice wins the game. 

The game starts with the number `n` on the chalkboard. Alice and Bob take turns choosing a divisor `x` of `n` such that `0 < x < n` and replacing `n` with `n - x`. If `n` is a prime number, `x` must also be a prime number. If a player cannot make a move, they lose the game.
"""

def divisorGame(n):
    def is_prime(num):
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

    game = [0]*(n+1)
    game[1] = 0
    game[2] = 1

    for i in range(3, n+1):
        if is_prime(i):
            game[i] = not game[i-1]
        else:
            for j in range(1, i//2+1):
                if i%j == 0:
                    if game[i-j] == 0:
                        game[i] = 1
                        break

    return bool(game[n])