"""
QUESTION:
It was decided in IT City to distinguish successes of local IT companies by awards in the form of stars covered with gold from one side. To order the stars it is necessary to estimate order cost that depends on the area of gold-plating. Write a program that can calculate the area of a star.

A "star" figure having n ≥ 5 corners where n is a prime number is constructed the following way. On the circle of radius r n points are selected so that the distances between the adjacent ones are equal. Then every point is connected by a segment with two maximally distant points. All areas bounded by the segments parts are the figure parts. [Image] 


-----Input-----

The only line of the input contains two integers n (5 ≤ n < 10^9, n is prime) and r (1 ≤ r ≤ 10^9) — the number of the star corners and the radius of the circumcircle correspondingly.


-----Output-----

Output one number — the star area. The relative error of your answer should not be greater than 10^{ - 7}.


-----Examples-----
Input
7 10

Output
108.395919545675
"""

from math import tan, pi

def calculate_star_area(n: int, r: int) -> float:
    """
    Calculate the area of a star with n corners and a circumcircle radius r.

    Parameters:
    n (int): The number of star corners (prime number, 5 ≤ n < 10^9).
    r (int): The radius of the circumcircle (1 ≤ r ≤ 10^9).

    Returns:
    float: The area of the star with a relative error not greater than 10^{-7}.
    """
    a = tan(pi / (2 * n))
    b = tan(pi / n)
    a = 1 / a + 1 / b
    return r * r / a * n