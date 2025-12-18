"""
QUESTION:
As we all know Barney's job is "PLEASE" and he has not much to do at work. That's why he started playing "cups and key". In this game there are three identical cups arranged in a line from left to right. Initially key to Barney's heart is under the middle cup. $\left. \begin{array}{l}{\text{Rey}} \\{\text{to my}} \\{\text{heart}} \end{array} \right.$ 

Then at one turn Barney swaps the cup in the middle with any of other two cups randomly (he choses each with equal probability), so the chosen cup becomes the middle one. Game lasts n turns and Barney independently choses a cup to swap with the middle one within each turn, and the key always remains in the cup it was at the start.

After n-th turn Barney asks a girl to guess which cup contains the key. The girl points to the middle one but Barney was distracted while making turns and doesn't know if the key is under the middle cup. That's why he asked you to tell him the probability that girl guessed right.

Number n of game turns can be extremely large, that's why Barney did not give it to you. Instead he gave you an array a_1, a_2, ..., a_{k} such that  $n = \prod_{i = 1}^{k} a_{i}$ 

in other words, n is multiplication of all elements of the given array.

Because of precision difficulties, Barney asked you to tell him the answer as an irreducible fraction. In other words you need to find it as a fraction p / q such that $\operatorname{gcd}(p, q) = 1$, where $gcd$ is the greatest common divisor. Since p and q can be extremely large, you only need to find the remainders of dividing each of them by 10^9 + 7.

Please note that we want $gcd$ of p and q to be 1, not $gcd$ of their remainders after dividing by 10^9 + 7.


-----Input-----

The first line of input contains a single integer k (1 ≤ k ≤ 10^5) — the number of elements in array Barney gave you.

The second line contains k integers a_1, a_2, ..., a_{k} (1 ≤ a_{i} ≤ 10^18) — the elements of the array.


-----Output-----

In the only line of output print a single string x / y where x is the remainder of dividing p by 10^9 + 7 and y is the remainder of dividing q by 10^9 + 7.


-----Examples-----
Input
1
2

Output
1/2

Input
3
1 1 1

Output
0/1
"""

def calculate_key_probability(k: int, a: list[int]) -> str:
    """
    Calculate the probability that the girl guessed right after n turns of the game.

    Parameters:
    k (int): The number of elements in the array.
    a (list[int]): The array of integers where each element is a factor of n.

    Returns:
    str: The probability as an irreducible fraction in the form "x/y", where x and y are the remainders
         of dividing p and q by 10^9 + 7 respectively.
    """
    m = 1000000007
    (n, d) = (2, 1)
    for q in a:
        (d, n) = (q & d, pow(n, q, m))
    n = n * pow(2, m - 2, m) % m
    k = (n + 1 - 2 * d) * pow(3, m - 2, m) % m
    return f"{k}/{n}"