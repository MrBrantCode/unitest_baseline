"""
QUESTION:
Given two linked list of size N1 and N2 respectively of distinct elements, your task is to complete the function countPairs(), which returns the count of all pairs from both lists whose sum is equal to the given value X.
Note: The 2 numbers of a pair should be parts of different lists.
Example 1:
Input:
L1 = 1->2->3->4->5->6
L2 = 11->12->13
X = 15
Output: 3
Explanation: There are 3 pairs that
add up to 15 : (4,11) , (3,12) and (2,13)
Example 2:
Input:
L1 = 7->5->1->3
L2 = 3->5->2->8
X = 10
Output: 2
Explanation: There are 2 pairs that add up
to 10 : (7,3) and (5,5)
Your Task:
You only need to implement the given function countPairs() and return the count.
Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(N+M)
Constraints:
1<=size of linked list<=10000
1<=X<=10000
Note : All elements in a linked list are unique.
"""

def count_pairs(list1, list2, target_sum):
    # Create dictionaries to store the frequency of elements in both lists
    freq1 = {}
    freq2 = {}
    
    # Populate the frequency dictionary for list1
    for num in list1:
        if num in freq1:
            freq1[num] += 1
        else:
            freq1[num] = 1
    
    # Populate the frequency dictionary for list2
    for num in list2:
        if num in freq2:
            freq2[num] += 1
        else:
            freq2[num] = 1
    
    # Count the pairs whose sum equals the target_sum
    count = 0
    for num in freq1:
        complement = target_sum - num
        if complement in freq2:
            count += 1
    
    return count