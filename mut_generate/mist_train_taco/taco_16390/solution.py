"""
QUESTION:
You know that 1 kg of pulp can be used to make 1000 pages and 1 notebook consists of 100 pages. 

Suppose a notebook factory receives N kg of pulp, how many notebooks can be made from that?

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case contains a single integer N - the weight of the pulp the factory has (in kgs).

------ Output Format ------ 

For each test case, output the number of notebooks that can be made using N kgs of pulp.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 100$

----- Sample Input 1 ------ 
3
1
100
50

----- Sample Output 1 ------ 
10
1000
500

----- explanation 1 ------ 
Test case-1: $1$ kg of pulp can be used to make $1000$ pages which can be used to make $10$ notebooks.

Test case-2: $100$ kg of pulp can be used to make $100000$ pages which can be used to make $1000$ notebooks.

Test case-3: $50$ kg of pulp can be used to make $50000$ pages which can be used to make $500$ notebooks.
"""

def calculate_notebooks(pulp_weight: int) -> int:
    """
    Calculate the number of notebooks that can be made from a given weight of pulp.

    Args:
        pulp_weight (int): The weight of the pulp in kilograms.

    Returns:
        int: The number of notebooks that can be made from the given weight of pulp.
    """
    pages_per_kg = 1000
    pages_per_notebook = 100
    total_pages = pulp_weight * pages_per_kg
    notebooks = total_pages // pages_per_notebook
    return notebooks