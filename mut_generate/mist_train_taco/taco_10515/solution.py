"""
QUESTION:
Igor is a post-graduate student of chemistry faculty in Berland State University (BerSU). He needs to conduct a complicated experiment to write his thesis, but laboratory of BerSU doesn't contain all the materials required for this experiment.

Fortunately, chemical laws allow material transformations (yes, chemistry in Berland differs from ours). But the rules of transformation are a bit strange.

Berland chemists are aware of n materials, numbered in the order they were discovered. Each material can be transformed into some other material (or vice versa). Formally, for each i (2 ≤ i ≤ n) there exist two numbers x_{i} and k_{i} that denote a possible transformation: k_{i} kilograms of material x_{i} can be transformed into 1 kilogram of material i, and 1 kilogram of material i can be transformed into 1 kilogram of material x_{i}. Chemical processing equipment in BerSU allows only such transformation that the amount of resulting material is always an integer number of kilograms.

For each i (1 ≤ i ≤ n) Igor knows that the experiment requires a_{i} kilograms of material i, and the laboratory contains b_{i} kilograms of this material. Is it possible to conduct an experiment after transforming some materials (or none)?


-----Input-----

The first line contains one integer number n (1 ≤ n ≤ 10^5) — the number of materials discovered by Berland chemists.

The second line contains n integer numbers b_1, b_2... b_{n} (1 ≤ b_{i} ≤ 10^12) — supplies of BerSU laboratory.

The third line contains n integer numbers a_1, a_2... a_{n} (1 ≤ a_{i} ≤ 10^12) — the amounts required for the experiment.

Then n - 1 lines follow. j-th of them contains two numbers x_{j} + 1 and k_{j} + 1 that denote transformation of (j + 1)-th material (1 ≤ x_{j} + 1 ≤ j, 1 ≤ k_{j} + 1 ≤ 10^9).


-----Output-----

Print YES if it is possible to conduct an experiment. Otherwise print NO.


-----Examples-----
Input
3
1 2 3
3 2 1
1 1
1 1

Output
YES

Input
3
3 2 1
1 2 3
1 1
1 2

Output
NO
"""

def can_conduct_experiment(n, b, a, transformations):
    """
    Determines if the experiment can be conducted based on the available supplies and required amounts of materials,
    considering the given transformation rules.

    Parameters:
    - n (int): The number of materials.
    - b (list[int]): List of integers representing the supplies of each material in the laboratory.
    - a (list[int]): List of integers representing the amounts required for the experiment.
    - transformations (list[tuple[int, int]]): List of tuples representing the transformation rules for each material.

    Returns:
    - bool: True if the experiment can be conducted, False otherwise.
    """
    # Calculate the difference between available and required amounts
    b = [b[i] - a[i] for i in range(n)]
    
    # Initialize the transformation rules
    c = [[0, 0]] + transformations
    
    # Process the transformations from the last material to the first
    for i in range(n - 1, 0, -1):
        fa = c[i][0] - 1
        if b[i] >= 0:
            b[fa] += b[i]
        else:
            b[fa] += b[i] * c[i][1]
            if b[fa] < -1e+17:
                return False
    
    # Check if the first material has enough after all transformations
    return b[0] >= 0