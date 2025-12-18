"""
QUESTION:
Arthur has bought a beautiful big table into his new flat. When he came home, Arthur noticed that the new table is unstable.

In total the table Arthur bought has n legs, the length of the i-th leg is l_{i}.

Arthur decided to make the table stable and remove some legs. For each of them Arthur determined number d_{i} — the amount of energy that he spends to remove the i-th leg.

A table with k legs is assumed to be stable if there are more than half legs of the maximum length. For example, to make a table with 5 legs stable, you need to make sure it has at least three (out of these five) legs of the maximum length. Also, a table with one leg is always stable and a table with two legs is stable if and only if they have the same lengths.

Your task is to help Arthur and count the minimum number of energy units Arthur should spend on making the table stable.


-----Input-----

The first line of the input contains integer n (1 ≤ n ≤ 10^5) — the initial number of legs in the table Arthur bought.

The second line of the input contains a sequence of n integers l_{i} (1 ≤ l_{i} ≤ 10^5), where l_{i} is equal to the length of the i-th leg of the table.

The third line of the input contains a sequence of n integers d_{i} (1 ≤ d_{i} ≤ 200), where d_{i} is the number of energy units that Arthur spends on removing the i-th leg off the table.


-----Output-----

Print a single integer — the minimum number of energy units that Arthur needs to spend in order to make the table stable.


-----Examples-----
Input
2
1 5
3 2

Output
2

Input
3
2 4 4
1 1 1

Output
0

Input
6
2 2 1 1 3 3
4 3 5 5 2 1

Output
8
"""

def calculate_min_energy_to_stabilize_table(n, leg_lengths, energy_costs):
    MAX_D = 201
    
    # Combine leg lengths and energy costs into a list of tuples
    legs = sorted(zip(leg_lengths, energy_costs))
    
    # Calculate the suffix sum of energy costs
    d_suffix = [legs[0][1]]
    for i in range(1, n):
        d_suffix.append(d_suffix[-1] + legs[i][1])
    
    # Initialize the answer with the total energy cost
    ans = d_suffix[-1]
    
    # Dictionary to count the occurrences of each energy cost
    cnt = {}
    
    left = 0
    right = 0
    
    while left < n:
        # Move right pointer to the end of the current length group
        while right < n and legs[left][0] == legs[right][0]:
            right += 1
        
        # Calculate the number of legs to remove to make the table stable
        to_remove = left - (right - left - 1)
        
        # Calculate the current energy cost if we remove legs to the right
        curr_d = d_suffix[-1] - d_suffix[right - 1]
        
        # Use the energy costs dictionary to minimize the energy cost
        for i in range(1, MAX_D):
            if to_remove <= 0:
                break
            used = min(to_remove, cnt.get(i, 0))
            to_remove -= used
            curr_d += used * i
        
        # Update the answer with the minimum energy cost found
        ans = min(ans, curr_d)
        
        # Update the energy costs dictionary with the current group of legs
        while left < right:
            cnt[legs[left][1]] = cnt.get(legs[left][1], 0) + 1
            left += 1
    
    return ans