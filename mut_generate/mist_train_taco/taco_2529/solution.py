"""
QUESTION:
There are n stone quarries in Petrograd.

Each quarry owns mi dumpers (1 ≤ i ≤ n). It is known that the first dumper of the i-th quarry has xi stones in it, the second dumper has xi + 1 stones in it, the third has xi + 2, and the mi-th dumper (the last for the i-th quarry) has xi + mi - 1 stones in it.

Two oligarchs play a well-known game Nim. Players take turns removing stones from dumpers. On each turn, a player can select any dumper and remove any non-zero amount of stones from it. The player who cannot take a stone loses.

Your task is to find out which oligarch will win, provided that both of them play optimally. The oligarchs asked you not to reveal their names. So, let's call the one who takes the first stone «tolik» and the other one «bolik».

Input

The first line of the input contains one integer number n (1 ≤ n ≤ 105) — the amount of quarries. Then there follow n lines, each of them contains two space-separated integers xi and mi (1 ≤ xi, mi ≤ 1016) — the amount of stones in the first dumper of the i-th quarry and the number of dumpers at the i-th quarry.

Output

Output «tolik» if the oligarch who takes a stone first wins, and «bolik» otherwise.

Examples

Input

2
2 1
3 2


Output

tolik


Input

4
1 1
1 1
1 1
1 1


Output

bolik
"""

def determine_winner(n, quarries):
    """
    Determines the winner of the Nim game between two oligarchs, given the number of quarries and their respective dumpers.

    Parameters:
    n (int): The number of quarries.
    quarries (list of tuples): A list where each tuple contains two integers (xi, mi) representing the initial number of stones in the first dumper and the number of dumpers for each quarry.

    Returns:
    str: The winner of the game, either "tolik" or "bolik".
    """
    def xor_range(n):
        return [n, 1, n + 1, 0][n % 4]
    
    xor = 0
    for xi, mi in quarries:
        xor ^= xor_range(xi - 1) ^ xor_range(xi + mi - 1)
    
    return 'tolik' if xor != 0 else 'bolik'