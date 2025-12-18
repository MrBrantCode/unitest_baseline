"""
QUESTION:
Vector Willman and Array Bolt are the two most famous athletes of Byteforces. They are going to compete in a race with a distance of L meters today.

 [Image] 

Willman and Bolt have exactly the same speed, so when they compete the result is always a tie. That is a problem for the organizers because they want a winner. 

While watching previous races the organizers have noticed that Willman can perform only steps of length equal to w meters, and Bolt can perform only steps of length equal to b meters. Organizers decided to slightly change the rules of the race. Now, at the end of the racetrack there will be an abyss, and the winner will be declared the athlete, who manages to run farther from the starting point of the the racetrack (which is not the subject to change by any of the athletes). 

Note that none of the athletes can run infinitely far, as they both will at some moment of time face the point, such that only one step further will cause them to fall in the abyss. In other words, the athlete will not fall into the abyss if the total length of all his steps will be less or equal to the chosen distance L.

Since the organizers are very fair, the are going to set the length of the racetrack as an integer chosen randomly and uniformly in range from 1 to t (both are included). What is the probability that Willman and Bolt tie again today?


-----Input-----

The first line of the input contains three integers t, w and b (1 ≤ t, w, b ≤ 5·10^18) — the maximum possible length of the racetrack, the length of Willman's steps and the length of Bolt's steps respectively.


-----Output-----

Print the answer to the problem as an irreducible fraction [Image]. Follow the format of the samples output.

The fraction [Image] (p and q are integers, and both p ≥ 0 and q > 0 holds) is called irreducible, if there is no such integer d > 1, that both p and q are divisible by d.


-----Examples-----
Input
10 3 2

Output
3/10

Input
7 1 2

Output
3/7



-----Note-----

In the first sample Willman and Bolt will tie in case 1, 6 or 7 are chosen as the length of the racetrack.
"""

def calculate_tie_probability(t: int, w: int, b: int) -> tuple:
    """
    Calculate the probability that Willman and Bolt tie in a race with a maximum possible length of t meters,
    given that Willman's step length is w meters and Bolt's step length is b meters.

    Parameters:
    t (int): The maximum possible length of the racetrack.
    w (int): The length of Willman's steps.
    b (int): The length of Bolt's steps.

    Returns:
    tuple: A tuple (p, q) representing the irreducible fraction of the probability that Willman and Bolt tie.
    """
    
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    lc = lcm(w, b)
    mn = min(w, b)
    ans = mn * (t // lc + 1) - 1
    val = t // lc * lc + mn - 1
    if t - val < 0:
        ans += t - val
    g = gcd(ans, t)
    ans //= g
    t //= g
    return (ans, t)