"""
QUESTION:
Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character.
 
Example 1:
Input: s = abccc, k = 1
Output: 6
Explaination:
We remove c to get the value as 1^{2} + 1^{2} + 2^{2}
 
Example 2:
Input: s = aabcbcbcabcc, k = 3
Output: 27
Explaination: We remove two 'c' and one 'b'. 
Now we get the value as 3^{2 }+ 3^{2} + 3^{2}.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minValue() which takes s and k as input parameters and returns the minimum possible required value.
 
Expected Time Complexity: O(N+Klog(P))  where N is the length of string and P is number of distinct alphabets and K number of alphabets to be removed 
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ k ≤ |string length| ≤ 100
"""

def min_value_after_removal(s: str, k: int) -> int:
    from collections import Counter
    import heapq

    # Count the frequency of each character
    freq = Counter(s)
    
    # Create a max heap (using negative values to simulate max heap)
    max_heap = [-count for count in freq.values()]
    heapq.heapify(max_heap)
    
    # Perform k removals
    for _ in range(k):
        # Get the character with the highest frequency
        max_freq = -heapq.heappop(max_heap)
        # Decrease the frequency by 1
        max_freq -= 1
        # Push the updated frequency back into the heap
        heapq.heappush(max_heap, -max_freq)
    
    # Calculate the minimum value
    min_value = sum(count * count for count in max_heap)
    
    return min_value