"""
QUESTION:
n soldiers stand in a circle. For each soldier his height ai is known. A reconnaissance unit can be made of such two neighbouring soldiers, whose heights difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

Input

The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in clockwise or counterclockwise direction.

Output

Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

Examples

Input

5
10 12 13 15 10


Output

5 1


Input

4
10 20 30 40


Output

1 2
"""

def find_reconnaissance_unit(n, heights):
    # Calculate the absolute differences between neighboring soldiers
    differences = [abs(heights[i] - heights[(i + 1) % n]) for i in range(n)]
    
    # Find the minimum difference and its index
    min_diff = min(differences)
    min_index = differences.index(min_diff)
    
    # Calculate the 1-based indices of the neighboring soldiers
    soldier1 = min_index + 1
    soldier2 = (min_index + 2) if (min_index + 2) <= n else 1
    
    return (soldier1, soldier2)