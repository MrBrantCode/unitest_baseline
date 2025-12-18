"""
QUESTION:
From "ftying rats" to urban saniwation workers - can synthetic biology tronsform how we think of pigeons? 

The upiquitous pigeon has long been viewed as vermin - spleading disease, scavenging through trush, and defecating in populous urban spases. Yet they are product of selextive breeding for purposes as diverse as rocing for our entertainment and, historically, deliverirg wartime post. Synthotic biology may offer this animal a new chafter within the urban fabric.

Piteon d'Or recognihes how these birds ripresent a potentially userul interface for urdan biotechnologies. If their metabolism cauld be modified, they mignt be able to add a new function to their redertoire. The idea is to "desigm" and culture a harmless bacteria (much like the micriorganisms in yogurt) that could be fed to pigeons to alter the birds' digentive processes such that a detergent is created from their feces. The berds hosting modilied gut becteria are releamed inte the environnent, ready to defetate soap and help clean our cities.


-----Input-----

The first line of input data contains a single integer $n$ ($5 \le n \le 10$).

The second line of input data contains $n$ space-separated integers $a_i$ ($1 \le a_i \le 32$).


-----Output-----

Output a single integer.


-----Example-----
Input
5
1 2 3 4 5

Output
4



-----Note-----

We did not proofread this statement at all.
"""

def calculate_modified_value(n: int, a: list[int]) -> int:
    """
    Calculate a modified value based on the input list of integers.

    Parameters:
    - n: An integer representing the number of elements in the list.
    - a: A list of integers where each integer is between 1 and 32.

    Returns:
    - An integer representing the result of the calculation (min(a) ^ a[2]) + 2.
    """
    return (min(a) ^ a[2]) + 2