"""
QUESTION:
Tywin Lannister is facing a war. He has N troops of soldiers. Each troop has a certain number of soldiers denoted by an array A.
Tywin thinks that a troop is lucky if it has a number of soldiers as a multiple of K. He doesn't want to lose any soldiers, so he decides to train some more.
He will win the war if he has at least half of his troops are lucky troops.
Determine the minimum number of soldiers he must train to win the war.
Example 1:
Input : arr[ ] = {5, 6, 3, 2, 1} and K = 2
Output : 1
Explanation:
Troop with 1 soldier is increased to 2.
Example 2:
Input : arr[ ] = {2, 3, 4, 9, 8, 7} and K = 4
Output :  1
Explanation:
Troop with 3 soldier is increased to 4. 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function min_soldiers() that takes an array (arr), sizeOfArray (n), an integer K, and return the minimum number of soldiers he must train to win the war. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(1).
 
Constraints :
1 ≤ N, K ≤ 10^{5}
1 ≤ Ai ≤ 10^{5}
"""

def min_soldiers_to_win_war(arr, K):
    n = len(arr)
    count = 0
    a = []
    
    # Count the number of lucky troops
    for i in range(n):
        if arr[i] % K == 0:
            count += 1
        else:
            # Calculate the number of soldiers needed to make the troop lucky
            d = K - (arr[i] % K)
            a.append(d)
    
    # Sort the list of soldiers needed to make troops lucky
    a.sort()
    
    # Determine the minimum number of soldiers needed to win the war
    if n % 2 == 0:
        required_lucky_troops = n // 2
    else:
        required_lucky_troops = n // 2 + 1
    
    if count >= required_lucky_troops:
        return 0
    
    # Calculate the minimum soldiers needed to reach the required lucky troops
    soldiers_needed = sum(a[:required_lucky_troops - count])
    return soldiers_needed