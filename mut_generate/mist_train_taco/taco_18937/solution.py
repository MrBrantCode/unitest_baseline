"""
QUESTION:
Charul has been given a task by Ishaan. He challenges him to fill a large container of capacity K liters. Charul has N vessels with him with different capacities.
The capacities of the vessels are given by an array A. The condition is that the container should be filled up to the brim but no water should be wasted in overflowing. Also, the vessels can't be filled partially.
Determine if Charul can fill up the container with the given conditions or not.
Assume that Charul has an unlimited supply of water.
 
Example 1:
Input: 
arr[ ] = {6, 3, 4, 2, 1} and K = 20
Output: 
1
Explanation:
The container can be filled in the following manner : 
Add water using the 6 litre vessel 3 times :
Container filled upto 18 litres
Add water using the 2 litre vessel 1 time : 
Container filled upto 20 litres
Example 2:
Input: 
arr[] = {2, 4, 3} and K = 15 
Output:  
1
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function vessel() that takes an array (arr), sizeOfArray (n), an integer K, and return the array return true if it is possible else return false. The driver code takes care of the printing.
Expected Time Complexity: O(N*K).
Expected Auxiliary Space: O(X). where X is the maximum element in an array.
Constraints : 
1 ≤ N ≤ 100
1 ≤ K ≤ 10^{3}
1 ≤ A[i] ≤ 100
"""

def can_fill_container(arr, K):
    store = set([K])
    for item in arr:
        temp = set()
        for num in store:
            while num - item >= 0:
                num -= item
                temp.add(num)
        if 0 in temp:
            return True
        store.update(temp)
    return False