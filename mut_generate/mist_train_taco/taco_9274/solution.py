"""
QUESTION:
There are n pictures delivered for the new exhibition. The i-th painting has beauty a_{i}. We know that a visitor becomes happy every time he passes from a painting to a more beautiful one.

We are allowed to arranged pictures in any order. What is the maximum possible number of times the visitor may become happy while passing all pictures from first to last? In other words, we are allowed to rearrange elements of a in any order. What is the maximum possible number of indices i (1 ≤ i ≤ n - 1), such that a_{i} + 1 > a_{i}.


-----Input-----

The first line of the input contains integer n (1 ≤ n ≤ 1000) — the number of painting.

The second line contains the sequence a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 1000), where a_{i} means the beauty of the i-th painting.


-----Output-----

Print one integer — the maximum possible number of neighbouring pairs, such that a_{i} + 1 > a_{i}, after the optimal rearrangement.


-----Examples-----
Input
5
20 30 10 50 40

Output
4

Input
4
200 100 100 200

Output
2



-----Note-----

In the first sample, the optimal order is: 10, 20, 30, 40, 50.

In the second sample, the optimal order is: 100, 200, 100, 200.
"""

def max_happy_visitor_count(n, beauties):
    # Create a frequency array to count occurrences of each beauty value
    frequency = [0] * 1001
    
    # Fill the frequency array
    for beauty in beauties:
        frequency[beauty] += 1
    
    # Create a list to store the optimal order of beauties
    optimal_order = []
    
    # Fill the optimal order list by iterating through the frequency array
    for beauty in range(1001):
        while frequency[beauty] > 0:
            optimal_order.append(beauty)
            frequency[beauty] -= 1
    
    # Calculate the number of happy transitions
    happy_count = 0
    for i in range(1, len(optimal_order)):
        if optimal_order[i] > optimal_order[i - 1]:
            happy_count += 1
    
    return happy_count